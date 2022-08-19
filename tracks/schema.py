import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Track, Like


class TrackType(DjangoObjectType):
    class Meta:
        model = Track
        fields = '__all__'


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = '__all__'


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType, search=graphene.String())
    likes = graphene.List(LikeType)

    def resolve_tracks(self, info, search=None):
        if search:
            return Track.objects.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(url__icontains=search) |
                Q(posted_by__username__icontains=search)
            ).distinct()
        return Track.objects.all()

    def resolve_likes(self, info):
        return Like.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        user = info.context.user
        if user.is_authenticated:
            track = Track.objects.create(title=title, description=description, url=url)
            return CreateTrack(track=track)
        raise GraphQLError('user is not authenticated')


class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, track_id, **kwargs):
        track = Track.objects.filter(id=track_id)
        if track:
            if info.context.user == track.first().posted_by:
                track.update(**kwargs)
                return UpdateTrack(track=track.first())
            raise GraphQLError('you are not authorized to update this post')
        raise GraphQLError('this Track does not exists')


class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, track_id):
        try:
            track = Track.objects.get(id=track_id)
            if info.context.user is track.posted_by:
                track.delete()
                return UpdateTrack(track_id=track_id)
            raise GraphQLError('you are not authorized to delete this post')
        except Track.DoesNotExist:
            raise GraphQLError('this Track does not exists')


class CreateLike(graphene.Mutation):
    like = graphene.Field(LikeType)

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, track_id):
        try:
            track = Track.objects.get(id=track_id)
            user = info.context.user
            if user.is_authenticated:
                like = Like.objects.create(user=user, track=track)
                return CreateLike(like=like)
            raise GraphQLError('you are not Authenticated')
        except Track.DoesNotExist:
            raise GraphQLError('this Track does not exists')


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()

    create_like = CreateLike.Field()
