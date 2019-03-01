from django.contrib import admin

from runapp.models import Isue, IsueAdmin, Keys_List, Keys_ListAdmin, GUrl_List, GUrl_ListAdmin,Excludespage,ExcludespageAdmin,Excludestate,ExcludestateAdmin
from runapp.models import Fromproxy
from runapp.models import Proxy_ListAdmin, Proxy_List

admin.site.register(Isue, IsueAdmin)
admin.site.register(Keys_List, Keys_ListAdmin)
admin.site.register(GUrl_List, GUrl_ListAdmin)
admin.site.register(Excludespage, ExcludespageAdmin)
admin.site.register(Excludestate, ExcludestateAdmin)
admin.site.register(Fromproxy)
admin.site.register(Proxy_List, Proxy_ListAdmin)

