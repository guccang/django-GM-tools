from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context
from mysite.forms import blackform,restoreform,configform,userinfoform
#for django form
from django.template.context_processors import csrf
# http redirect
from django.http import HttpResponseRedirect

###################################
import http.client
import urllib
import urllib.request
import urllib.error
from django.contrib.auth.decorators import login_required

GAME_SERVER_HOST = '127.0.0.1'
GAME_SERVER_PORT = 8036
    
def getGSInfo(test_data):
    try:
        test_data.encode('utf-8')
        url = ('http://%s:%d/Service.aspx/webBackOffice' % (GAME_SERVER_HOST,GAME_SERVER_PORT))
        headerdata={'Host':GAME_SERVER_HOST}
        conn = http.client.HTTPConnection(GAME_SERVER_HOST,GAME_SERVER_PORT)
        conn.request(method="POST",url=url,body=test_data,headers=headerdata)
        response=conn.getresponse()
        res = response.read()
        #result = "type:"+str((res))
        if None == res :
            result = "error"
        else:
            result = res.decode('utf-8')
    except :
        result = '网络错误'
        
    return result
#####################################
#@login_required
def runtime(request):
    #if False == request.user.is_authenticated():
    #     return HttpResponseRedirect('/admin/login')
         
    c = {}
    username = request.user.username
    if not username :
        username = '游客'
    c['username'] = username
        
        
    menu = {}
    menu[username] = '/admin'
    menu['black'] = 'black'
    menu['addHappyPoint'] = 'http://www.google.com'
    menu['LogOut'] = '/admin/logout'
    menu['admin'] = '/admin'
    menu['restore'] = 'restore'
    menu['config'] = 'config'
    menu['userinfo'] = 'userinfo'


    c['isMenu'] = 'yes'
    c['dic'] = menu
    c['keys'] = sorted(menu)
    return render_to_response('runtime/cmdMenu.html',c)

def blackInfo():
    preCmd = 'blackInfo:10' 
    preInfo = getGSInfo(preCmd)
    preList =  preInfo.split(',')
    return preList
    
def restoreInfo():
    preList = []
    preList.append('UserRankingTotal:30000,积分榜数据导入')
    preList.append('UserRanking:30000,排行榜数据导入')
    preList.append('HappyModeData:30000,欢乐无尽数据导入')
    preList.append('GameUser:30000,玩家数据导入，然而你可以看到，太jb2222222')
    return preList
    

def has_perm(request,c):
     #登录验证
    if False == request.user.is_authenticated():
        c['errorpage'] = HttpResponseRedirect('/admin/login')
        
     #权限验证
    if c['needSuper']:
        if False == request.user.is_superuser:
            c['notify'] = '没有相关权限，请联系管理员。'
            c['errorpage'] = render_to_response('runtime/NoPermission.html',c)
        else: 
            pass
    else:
        if False == request.user.has_perm(c['perm']):
            c['notify'] = '没有相关权限，请联系管理员。'
            c['errorpage'] =  render_to_response('runtime/NoPermission.html',c)
        else:
            pass
            
def userinfo(request):
    c={}
    c.update(csrf(request))
    c['needSuper'] = True
    has_perm(request,c)
    #ttt = type(c.get['errorpage'])
    if 'errorpage' in c:
        return c['errorpage']
        
    c['username'] = request.user.username
 
    if request.method == 'POST' :
        form = userinfoform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cmd = ('userInfo:%s,%d,%s,%d,%d' % (cd['cmd'],cd['id'],cd['name'],cd['ur_score'],cd['urt_score']))
            ret = getGSInfo(cmd)
            c['notify'] = '执行成功查看pre ，after块'
            c['after'] = ret
        else:
            pass
    else:
        c['notify'] = ''
        form = userinfoform()
    
    #c.pop('errorpage')
    c['form'] = form
    return render_to_response("runtime/userinfo.html",c)
 
def config(request):
     #登录验证
    if False == request.user.is_authenticated():
        return HttpResponseRedirect('/admin/login')
        
    c={}
    c.update(csrf(request))
    c['username'] = request.user.username
    
     #权限验证
    if False == request.user.has_perm('GM.add_activitymodel'):
        c['notify'] = '没有相关权限，请联系管理员。'
        return render_to_response('runtime/NoPermission.html',c)
  
    if request.method == 'POST':
        form = configform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cmd = 'updateConfig:'+form.cleaned_data['tableName']+','+'1000'
            ret = getGSInfo(cmd)
            c['notify'] = "执行成功,查看pre,after寻找结果"
            c['after'] = ret
        else:
            pass
    else:
        c['notify'] = '输入'
        form = configform(
        )
    
    #c['pre'] = restoreInfo()
    c['form'] = form
    return render_to_response("runtime/config.html",c)
    
def restore(request):
    #登录验证
    if False == request.user.is_authenticated():
        return HttpResponseRedirect('/admin/login')
        
    c={}
    c.update(csrf(request))
    c['username'] = request.user.username
    
     #权限验证
    if False == request.user.is_superuser:
        c['notify'] = '没有相关权限，请联系管理员。'
        return render_to_response('runtime/NoPermission.html',c)
        
    if request.method == 'POST':
        form = restoreform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cmd = 'doFrom:'+form.cleaned_data['tableName']+','+form.cleaned_data['parms']
            ret = getGSInfo(cmd)
            c['notify'] = "执行成功,查看pre,after寻找结果"
            c['after'] = ret
        else:
            pass
    else:
        c['notify'] = '输入'
        form = restoreform(
            initial={'tableName':'UserRankingTotal'}
        )
    
    c['pre'] = restoreInfo()
    c['form'] = form
    return render_to_response("runtime/restore.html",c)
    
#@login_required    
def black(request):
    
    #登录验证
    if False == request.user.is_authenticated():
        return HttpResponseRedirect('/admin/login')
 
    # 提交template的格式化
    c = {}     
    c.update(csrf(request))
    c['username'] = request.user.username
    
    #权限验证
    if False == request.user.has_perm('GM.add_blacklistdata'):
        c['notify'] = '没有黑名单相关权限，请联系管理员。'
        return render_to_response('runtime/NoPermission.html',c)
    
    if request.method == 'POST':
        form = blackform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cmd = 'black:'+str(form.cleaned_data['id'])
            ret = getGSInfo(cmd)
            c['notify'] = "执行成功,查看pre,after寻找结果"
            c['after'] = ret
        else:
            pass #do nothing
    else:
        c['notify'] = '请输入要删除的玩家在排行榜上的名次.'
        form = blackform(
            initial={'message':'作弊'}
        )
    
    c['pre'] = blackInfo()    
    c['form'] = form
    return render_to_response('runtime/black.html',c)
    
