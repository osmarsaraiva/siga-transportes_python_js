from django.contrib import admin

from .models import Niveis
from .models import Frotas
from .models import Cidades
from .models import LancarViagens
from .models import AcertosViagens
from .models import Clientes
from .models import Documentos
from .models import Empresas
from .models import Fornecedores
from .models import Funcionarios
from .models import LancarBaixaVeiculos
from .models import Veiculos
from .models import TiposVeiculos
from .models import LancarContabilidade
from .models import LancarFerias
from .models import LancarFinanceiroViagens
from .models import PlanoContas
from .models import Situacoes
from .models import Usuarios

admin.site.register(Niveis)
admin.site.register(Frotas)
admin.site.register(Cidades)
admin.site.register(LancarViagens)
admin.site.register(AcertosViagens)
admin.site.register(Clientes)
admin.site.register(Documentos)
admin.site.register(Empresas)
admin.site.register(Fornecedores)
admin.site.register(LancarBaixaVeiculos)
admin.site.register(Veiculos)
admin.site.register(TiposVeiculos)
admin.site.register(LancarContabilidade)
admin.site.register(LancarFerias)
admin.site.register(LancarFinanceiroViagens)
admin.site.register(PlanoContas)
admin.site.register(Situacoes)
admin.site.register(Usuarios)
admin.site.register(Funcionarios)

# Register your models here.
