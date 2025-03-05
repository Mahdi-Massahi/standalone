import shutil
from datetime import datetime

from django.core.files import File

import apps.main.models as MODELS
import apps.main.services.llm.models as LLM_MODELS
from apps.main.services.latex.latex import CVTemplate, generate, compile
from apps.main.services.llm.agent import agent_tailor_cv, get_agent_generate_cv_meta


def tailor_cv(tailor: MODELS.Tailor):
    if tailor.instruction is None and tailor.instruction == "":
        return

    experiences = MODELS.Experience.objects.filter(
        user=tailor.application.user,
    )
    carriers = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            type=exp.get_type_display(),
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting.strftime("%Y %b").upper() if exp.starting else None,
            ending=exp.ending.strftime("%Y %b").upper() if exp.ending else None,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.CARRIER
    ]
    educations = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            type=exp.get_type_display(),
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting.strftime("%Y %b").upper() if exp.starting else None,
            ending=exp.ending.strftime("%Y %b").upper() if exp.ending else None,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.EDUCATION
    ]
    projects = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            type=exp.get_type_display(),
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting.strftime("%Y %b").upper() if exp.starting else None,
            ending=exp.ending.strftime("%Y %b").upper() if exp.ending else None,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.PROJECT
    ]
    cv = LLM_MODELS.CVModel(
        summary="",
        title="",
        carriers=carriers,
        educations=educations,
        projects=projects,
        hard_skills=tailor.application.user.hard_skills,
        soft_skills=tailor.application.user.soft_skills,
    )

    response = agent_tailor_cv(
        position=LLM_MODELS.ApplicationModel(
            title=tailor.application.job_title,
            description=tailor.application.job_description,
        ),
        cv=cv,
        fullname=tailor.application.user.get_full_name(),
        instruction=tailor.instruction,
    )

    cv_template = CVTemplate.TEMPLATE_01

    latex_content = generate(
        cv_template=cv_template,
        data={
            "user": tailor.application.user.__dict__,
            "cv": response.cv,
        },
    )

    meta = get_agent_generate_cv_meta()
    meta["response"] = str(response)

    tailor.instruction = None
    tailor.latex = latex_content
    tailor.comment = response.comment
    tailor.fitness = response.fitness
    tailor.meta = meta

    # Generate a unique filename based on CV id and timestamp
    filename = (
        f"{tailor.application.user.first_name}_"
        f"{tailor.application.user.last_name}_"
        f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}.pdf"
    )

    # Compile LaTeX content into a PDF file
    output_dir = "./output"  # FIXME: use temp
    compiled_file = compile(
        template=cv_template,
        content=latex_content,
        output_dir=output_dir,
    )

    # Check if the file was successfully created
    try:
        with open(compiled_file, "rb") as pdf_file:
            tailor.file.save(filename, File(pdf_file), save=True)

    finally:
        shutil.rmtree(output_dir)

    tailor.save()
    return response


def tailor_ml(tailor: MODELS.Tailor): ...
