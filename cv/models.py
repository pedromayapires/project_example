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


class Course(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # when did it start
    from_date = models.DateTimeField()
    # when did it end
    to_date = models.DateTimeField()
    # physical location
    location = models.CharField(max_length=255, unique=True)


class LanguageLevel(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Language(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # from bad to great or equivalent
    level = models.ForeignKey(LanguageLevel, on_delete=models.PROTECT)


class Role(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Skill(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    # website
    site = models.CharField(max_length=255, unique=True, null=True)
    # physical location
    location = models.CharField(max_length=255, unique=True, null=True)


class Project(BaseModel):
    # summary or title of the project
    title = models.CharField(max_length=255, unique=True)
    # what was accomplished or the purpose of the project
    accomplished = models.TextField()
    # when did it start
    from_date = models.DateTimeField()
    # when did it end
    to_date = models.DateTimeField()

    # what roles were performed
    roles = models.ManyToManyField(Role)
    # what skills were used
    skills = models.ManyToManyField(Skill)
    # what was the consulting agency behind the client
    agency = models.ForeignKey(Company, null=True, on_delete=models.PROTECT)
    # what client
    client = models.ForeignKey(Company, on_delete=models.PROTECT)
