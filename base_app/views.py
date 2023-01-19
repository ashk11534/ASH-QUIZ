from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from .models import ExamCategory, Exam, Question, Option, CorrectAnswer, SubmittedAnswer

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    category = request.GET.get('category') if request.GET.get('category') != None else ''

    exam_categories = ExamCategory.objects.filter(name__icontains = category).order_by('-id')

    context = {'exam_categories': exam_categories}

    return render(request, 'base_app/index.html', context = context)


def exams_on_category(request, category_slug):

    category = get_object_or_404(ExamCategory, slug = category_slug)

    exams = Exam.objects.filter(category = category).order_by('-id')

    context = {'category': category, 'exams': exams}

    return render(request, 'base_app/exams.html', context = context)


@login_required(login_url='my-login')
def exam_questions(request, exam_slug):

    exam = Exam.objects.get(slug = exam_slug)

    questions = Question.objects.filter(exam__slug = exam_slug)

    total_questions = len(questions)

    answers_list = []

    correct_answers = []

    result_count = 0

    if request.method == 'POST':

        for key in request.POST.keys():

            if key == 'csrfmiddlewaretoken':

                continue

            # print(request.POST.get(key))

            question_id = int(key.split('-')[-1])

            question = Question.objects.get(id = question_id)

            # print(question.title, request.POST.get(key))

            correct_answer = CorrectAnswer.objects.get(question = question)

            answers_list.append(request.POST.get(key))

            correct_answers.append(correct_answer.option.title)

        for answer in answers_list:

            if answer in correct_answers:

                result_count = result_count + 1

        # print(result_count)

        exam.participants.add(request.user)

        submitted_answers = ', '.join(answers_list)

        already_submit_user = SubmittedAnswer.objects.filter(exam = exam, submit_user = request.user)

        if len(already_submit_user) > 0:

            already_submit_user.delete()
        
        SubmittedAnswer.objects.create(submitted_answers = submitted_answers, exam = exam, number_of_correct_answers = result_count, submit_user = request.user)

        return redirect('result', exam_slug = exam_slug, marks = result_count, total_questions = total_questions)



    options = Option.objects.all()

    if request.user.is_authenticated:

        try:

            submitted_answer = SubmittedAnswer.objects.get(exam = exam, submit_user = request.user)

            context = {'questions': questions, 'options': options, 'submitted_answer': submitted_answer}

        except SubmittedAnswer.DoesNotExist:

            context = {'questions': questions, 'options': options}

    else:

         context = {'questions': questions, 'options': options}


    return render(request, 'base_app/questions.html', context = context)


@login_required(login_url='my-login')
def result(request, exam_slug, marks, total_questions):

    context = {'exam_slug': exam_slug, 'marks': marks, 'total_questions': total_questions}

    return render(request, 'base_app/result.html', context = context)


@login_required(login_url='my-login')
def result_details(request, exam_slug):

    exam = Exam.objects.get(slug = exam_slug)

    questions = Question.objects.filter(exam__slug = exam_slug)

    correct_answers = CorrectAnswer.objects.filter(question__in = questions)

    correct_answer_option_titles = [answer.option.title for answer in correct_answers]

    options = Option.objects.all()

    if request.user.is_authenticated:

        try:

            submitted_answer = SubmittedAnswer.objects.get(exam = exam, submit_user = request.user)

            submitted_answers = submitted_answer.submitted_answers.split(', ')

            context = {'questions': questions, 'options': options, 'correct_answers': correct_answers, 'submitted_answers': submitted_answers, 'correct_answer_option_titles': correct_answer_option_titles}

        except SubmittedAnswer.DoesNotExist:

            context = {'questions': questions, 'options': options, 'correct_answers': correct_answers}

    else:

        context = {'questions': questions, 'options': options, 'correct_answers': correct_answers}

    return render(request, 'base_app/result-details.html', context = context)

    
    