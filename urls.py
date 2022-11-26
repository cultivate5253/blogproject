from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'blog'

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLが''(無し)の場合
    # viewsモジュールのIndexVieを実行
    path('', views.IndexView.as_view(), name='index'),
    
    # リクエストされたURLが「blog-detal/レコードのid/」の場合は
    # BlogDetalを実行
    path(
        # 詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を'blog_detail'にする
        name='blog_detail'
        ),
    # scienceカテゴリの一覧ページのURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは「science-list/」
        'science-list/',
        # viewsモジュールのBlogDetailを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name='science_list'
        ),
    # dailylifeカテゴリの一覧ページのURLパターン
    path(
        # dailylifeカテゴリの一覧ページのURLは「dailylife-list/」
        'dailylife-list/',
        # viewsモジュールのDailylifeViewを実行
        views.DailylifeView.as_view(),
        # URLパターンの名前を'dailylife_list'にする
        name='dailylife_list'
        ),
    # musicカテゴリの一覧ページのURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは「music-list/」
        'music-list/',
        # viewsモジュールのMusicViewを実行
        views.MusicView.as_view(),
        # URLパターンの名前を'music_list'にする
        name='music_list'
        ),
    # 問い合わせページのURLパターン
    path(
        # 問い合わせページのURLは「contact/」
        'contact/',
        # viewsモジュールのInquiryViewを実行
        views.ContactView.as_view(),
        # URLパターンの名前を'contact'にする
        name='contact'
        ),
]
