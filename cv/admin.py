from django.contrib import admin

from .models import (
    PersonalInfo,
    Course,
    LanguageLevel,
    Language,
    LanguageLearned,
    Role,
    Skill,
    Company,
    Project,
)

admin.site.register(PersonalInfo)
admin.site.register(Course)
admin.site.register(LanguageLevel)
admin.site.register(Language)
admin.site.register(LanguageLearned)
admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Project)
