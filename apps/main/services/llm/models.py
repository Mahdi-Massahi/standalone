from pydantic import BaseModel


class ExperienceModel(BaseModel):
    starting: str | None
    ending: str | None
    title: str
    type: str | None
    role: str
    location: str | None
    url: str | None
    description: str


class CVModel(BaseModel):
    summary: str
    title: str
    carriers: list[ExperienceModel]
    projects: list[ExperienceModel]
    educations: list[ExperienceModel]
    soft_skills: list[str]
    hard_skills: list[str]


class ApplicationModel(BaseModel):
    title: str
    description: str


class CVGeneratorModel(BaseModel):
    comment: str
    fitness: int
    cv: CVModel
