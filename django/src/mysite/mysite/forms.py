from django import forms

GG_Char_NotEmpty = 'must not be empty'
RESTORECHOICES = (
 ('------------','-----------'), # first field is invalid.
 ('UserRankingTotal','UserRankingTotal'),
 ('UserRanking','UserRanking'),
 ('HappyModeData','HappyModeData'),
 ('GameUser','GameUser'),
)

CONFIGFORMCHOICES=(
    ('--------','-------'),
    ('activitymodel','活动表'),
    ('happydatamodel','欢乐无尽表'),
    ('configuimodel','客户端UI配置表'),
)



class userinfoform(forms.Form):
    USERINFOCHOICES = (
        ('------','------'),
        ('get','get'),
        ('set','set'),
    )
    cmd = forms.ChoiceField(choices=USERINFOCHOICES)
    id = forms.IntegerField()
    name = forms.CharField()
    ur_score = forms.IntegerField()
    urt_score=forms.IntegerField()
    
    def clean_parms(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError(GG_Char_NotEmpty)
        return name
        
    
    
    
class configform(forms.Form):
    tableName = forms.ChoiceField(choices=CONFIGFORMCHOICES);
    #parms = forms.CharField()
     
    def clean_parms(self):
        tableName = self.cleaned_data['tableName']
        if tableName == '':
            raise forms.ValidationError(GG_Char_NotEmpty)
        return tableName
               
    #def clean_parms(self):
    #    parms = self.cleaned_data['parms']
    #    if parms == '':
    #        raise forms.ValidationError(GG_Char_NotEmpty)
    #    return parms
        
class restoreform(forms.Form):
    parms = forms.CharField()
    tableName = forms.ChoiceField(choices=RESTORECHOICES)
    
    def clean_tableName(self):
        tableName = self.cleaned_data['tableName']
        if tableName == '':
            raise forms.ValidationError(GG_Char_NotEmpty)
        return tableName
        
    def clean_parms(self):
        parms = self.cleaned_data['parms']
        if parms == '':
            raise forms.ValidationError(GG_Char_NotEmpty)
        return parms
        
class blackform(forms.Form):
    id = forms.IntegerField()
    info = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        if message=='':
            raise forms.ValidationError(GG_Char_NotEmpty)
        return message
        
    def clean_info(self):
        info = self.cleaned_data['info']
        myid   = self.cleaned_data['id']
        lst = info.split(':')
        if(lst[0] != str(myid)):
            raise forms.ValidationError('info filed is not match')
        
        return info
    def clean_id(self):
        id = self.cleaned_data['id']
        if id<0:
            raise forms.ValidationError('this must be > 0')
        return id

