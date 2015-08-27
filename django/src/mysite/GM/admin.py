from django.contrib import admin
from GM.models import Blacklistdata,Gameuser,Happymodedata,Userranking
from GM.models import Activitymodel
from GM.models import Configuimodel,Realinfodatamodel
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display=('descript','version','activityid','begin','end','parms',)
    list_filter = ('version','activityid',)
    ordering=('activityid','version',)
    fields=('version','activityid','parms','begin','end','descript')
    list_editable=('begin','end')
    list_display_links = ('descript',)
    #radio_fields = {'version':admin.HORIZONTAL,'activityid':admin.HORIZONTAL}
    
    actions = ['sync']
    def sync(self,request,queryset):
        pass
            
    sync.short_description = '同步到服务器'
    

admin.site.register(Blacklistdata)
admin.site.register(Gameuser)
admin.site.register(Happymodedata)
admin.site.register(Userranking)
admin.site.register(Configuimodel)
admin.site.register(Realinfodatamodel)
admin.site.register(Activitymodel,ActivityAdmin)
