from core.models import BaseModel, models


class PersonalInfo(BaseModel):
    name = models.CharField(max_length=255)
    intro = models.TextField()
    phone_number = models.CharField(max_length=255)
    # physical approximate location
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    languages = models.ManyToManyField(Skill)


class Course(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # when did it start
    from_date = models.DateField()
    # when did it end
    to_date = models.DateField()
    # physical location
    location = models.CharField(max_length=255, unique=True)


class LanguageLevel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # native is 1, fluent is 2 and so forth
    rank = models.IntField()


class Language(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class LanguageLearned(BaseModel):
    person = models.ForeignKey(PersonalInfo, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    # from bad to great or equivalent
    level = models.ForeignKey(LanguageLevel, on_delete=models.PROTECT)


class Role(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Skill(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # website
    site = models.CharField(max_length=255, null=True)
    # physical location
    location = models.CharField(max_length=255, null=True)


class Project(BaseModel):
    # summary or title of the project
    title = models.CharField(max_length=255, unique=True)
    # what was accomplished or the purpose of the project
    accomplished = models.TextField()
    # when did it start
    from_date = models.DateField()
    # when did it end
    to_date = models.DateField()

    # what was the consulting agency behind the client
    agency = models.ForeignKey(Company, null=True, on_delete=models.PROTECT)
    # what client, ideally there should be an option on the frontend to hide
    # the client in cases where there is an agency involved
    client = models.ForeignKey(Company, on_delete=models.PROTECT)
    # what roles were performed
    roles = models.ManyToManyField(Role)
    # what skills were used
    skills = models.ManyToManyField(Skill)
