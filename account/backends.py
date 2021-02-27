from django.contrib.auth.models import User

class EmailBackend(object):

    def authenticate(self,username=None,password=None,**kwargs):
        try:
            user = User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user=User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        if getattr(user,'is_active') and user.check_password(password):
            return User
        return None
    def get_user(self,user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


"""
        if AgentTable.objects.filter(username=username, password=password) or AgentTable.objects.filter(username=AgentTable.objects.get(email=username), password=password):

            return render(request, "agentProfile.html",{})
        else:
            return render(request, "agentLogin.html", {"msg": "invalid username or password"})"""