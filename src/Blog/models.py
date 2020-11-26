from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics', default='default.jpg', )
    ft_name = models.CharField(max_length=200, null=True)
    lt_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Profession = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=1000, null=True)


class BlogViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BlogCategories(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BlogComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(
        'Blog', related_name='blogcomments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # content = models.TextField()
    # content = HTMLField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(BlogCategories)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return BlogComments.objects.filter(blog=self).count()


class NewsLetterUser(models.Model):
    email = models.EmailField(max_length=70, default='example@email.com')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
