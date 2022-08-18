import graphene
from graphene_django import DjangoObjectType

from .models import Track, Like
from users.schema import UserType


class TrackType(DjangoObjectType):
    class Meta:
        model = Track
        fields = '__all__'


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


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
        raise Exception('user is not authenticated')


class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, track_id, **kwargs):
        try:
            track = Track.objects.get(id=track_id)
            if info.context.user is track.posted_by:
                track.update(**kwargs)
                return UpdateTrack(track=track)
            raise Exception('you are not authorized to update this post')
        except Track.DoesNotExist:
            raise Exception('this Track does not exists')


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
            raise Exception('you are not authorized to delete this post')
        except Track.DoesNotExist:
            raise Exception('this Track does not exists')


class CreateLike(graphene.Mutation):
    user = graphene.Field(UserType)
    track = graphene.Field(TrackType)

    class Arguments:
        # user_id = graphene.Int(required=True)
        track_id = graphene.Int(required=True)

    def mutate(self, info, track_id):
        try:
            track = Track.objects.get(id=track_id)
            user = info.context.user
            if user.is_authenticated:
                like = Like.objects.create(user=user, track=track)
                return CreateLike(user=user, track=track)
            raise Exception('you are not Authenticated')
        except Track.DoesNotExist:
            raise Exception('this Track does not exists')


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()

    create_like = CreateLike.Field()
