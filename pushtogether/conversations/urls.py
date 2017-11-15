from rest_framework.routers import SimpleRouter
from .views import (
    ConversationViewSet,
    ConversationReportViewSet,
    CommentViewSet,
    NextCommentViewSet,
    CommentReportViewSet,
    VoteViewSet,
    AuthorViewSet,
)

router = SimpleRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'conversations', ConversationViewSet, base_name='conversation')
router.register(r'comments', CommentViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'conversations-report', ConversationReportViewSet,
                base_name='conversation-report')
router.register(r'comments-report', CommentReportViewSet,
                base_name='comment-report')
router.register(r'next_comment', NextCommentViewSet,
                base_name='conversation-next-comment')

urlpatterns = router.urls
