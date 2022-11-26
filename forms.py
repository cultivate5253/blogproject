# django.formsをインポート
from django import forms
# django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
  # フォームのフィールドをクラス変数として定義
  name = forms.CharField(label='お名前')
  email = forms.EmailField(label='メールアドレス')
  title = forms.CharField(label='件名')
  message = forms.CharField(label='メッセージ', widget=forms.Textarea)
  
  def __init__(self, *args, **kwargs):
    '''ContactFormのコンストラクター
    
       フィールドの初期化を行う
    '''
    super().__init__(*args, **kwargs)
    # nameフィールドのplaceholderにメッセージを登録
    self.fields['name'].widget.attrs['placeholder'] = \
      'お名前を入力してください'
    # nameフィールドを出力する<input>タグのclass属性を設定
    self.fields['name'].widget.attrs['class'] = 'form-control'
    
    # emailフィールドのplaceholderにメッセージを登録
    self.fields['email'].widget.attrs['placeholder'] = \
      'メールアドレスを入力してください'
    # emailフィールドを出力する<input>タグのclass属性を設定
    self.fields['email'].widget.attrs['class'] = 'form-control'
    
    # titleフィールドのplaceholderにメッセージを登録
    self.fields['title'].widget.attrs['placeholder'] = \
      'タイトルを入力してください'
    # titleフィールドを出力する<input>タグのclass属性を設定
    self.fields['title'].widget.attrs['class'] = 'form-control'
    
    # messageフィールドのplaceholderにメッセージを登録
    self.fields['message'].widget.attrs['placeholder'] = \
      'メッセージを入力してください'
    # messageフィールドを出力する<input>タグのclass属性を設定
    self.fields['message'].widget.attrs['class'] = 'form-control'

  def send_email(self):
    '''フォームに入力された内容をメールで送信する
    
    '''
    # フォームに入力されたデータをフィールド名を指定して取得
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    title = self.cleaned_data['title']
    message = self.cleaned_data['message']
    # メールのタイトルの書式を設定
    subject = 'お問い合わせ: {}'.format(title)
    # フォームの入力データの書式を設定
    message = \
      '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
      .format(name, email, title, message)
    # メールの送信元のアドレス
    from_email = 'toshiyakinjo@gmail.com'
    # 送信先のメールアドレス
    to_list = ['t-kinjo@nifty.com']
    # EmailMessageオブジェクトを生成
    message = EmailMessage(subject=subject,
                           body=message,
                           from_email=from_email,
                           to=to_list,
                           )
    # EmailMessageクラスのsend()でメールサーバーからメールを送信
    message.send()
