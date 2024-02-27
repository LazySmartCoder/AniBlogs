from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "HomePage"),
    path("blogs", views.Blogs, name = "Blogs"),
    path("read-blog/<str:slug>", views.ReadBlog, name = "ReadBlog"),
    path("login", views.Login, name = "Login"),
    path("register", views.Register, name = "Register"),
    path("error", views.ErrorPage, name = "ErrorPage"),
    path("login-done", views.LoginDone, name = "LoginDone"),
    path("register-done", views.RegisterDone, name = "RegisterDone"),
    path("logout", views.Logout, name = "Logout"),
    path("user-profile", views.UserProfile, name = "UserProfile"),
    path("edit-userprofile", views.EditUserProfile, name = "EditUserProfile"),
    path("delete-account", views.DeleteAccount, name = "DeleteAccount"),
    path("verify-email", views.VerifyEmail, name = "VerifyEmail"),
    path("email-verified", views.EmailVerified, name = "EmailVerified"),
    path("resend-otp", views.ResendOTP, name = "ResendOTP"),
    path("change-password", views.ChangePassword, name = "ChangePassword"),
    path("search", views.Search, name = "Search"),
    path("post-comment", views.PostComment, name = "PostComment"),
    path("like-blog/<int:likeid>", views.LikeBlog, name = "LikeBlog"),
    path("cat/<str:catslug>", views.Cat, name = "Cat"),
    path("forgot-password", views.ForgotPassword, name = "ForgotPassword"),
    path("password-recovery", views.PasswordRecovery, name = "PasswordRecovery"),
    path("password-recovered", views.PasswordRecovered, name = "PasswordRecovered"),
    path("terms-and-conditions", views.TermsConditions, name = "TermsConditions"),
]