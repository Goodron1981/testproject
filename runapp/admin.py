from django.contrib import admin

from runapp.models import Isue, IsueAdmin, Keys_List, Keys_ListAdmin, GUrl_List, GUrl_ListAdmin,Excludespage,ExcludespageAdmin,Excludestate,ExcludestateAdmin
from runapp.models import Fromproxy

admin.site.register(Isue, IsueAdmin)
admin.site.register(Keys_List, Keys_ListAdmin)
admin.site.register(GUrl_List, GUrl_ListAdmin)
admin.site.register(Fromproxy)

