from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
import pdb

def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {
        'mynumbers':[1,2,3,4,5,6,],
        'firstName': 'Felix',
        'lastName': 'Wei',
        }) 

def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

def felixPageView(request):
    return render(request, 'felix.html')    


def homePost(request):
    # Use request object to extract choice.

    choice = -999
    gmat = -999 # Initialize gmat variable.

    try:
        # Extract value from request object by control name. 
        currentChoice = request.POST['choice']  
        gmatStr = request.POST['gmat']  

        # # Crude debugging effort. 
        # print("*** Years work experience: " + str(currentChoice))
        # choice    = int(currentChoice)
        # gmat = float(gmatStr)

        # print("Just before Felix's breakpoint")
        # pdb.set_trace()
        # breakpoint()
        # print("Just after breakpoint")
        # # Crude debugging effort.
        # print("*** Years work experience: " + str(currentChoice))


    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage':'*** The data submitted is invalid. Please try again.',
            'mynumbers': [1, 2, 3, 4, 5, 6, ]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'choice':choice,'gmat':gmat},))

def results(request, choice, gmat):
    print("*** Inside reults()")
    return render(request, 'results.html', {'choice': choice, 'gmat':gmat})


      
import pickle
import pandas as pd

def results(request, choice, gmat):
    print("*** Inside reults()")
    # load saved model
    with open("C:\model_pkl" , 'rb') as f:
        loadedModel = pickle.load(f)

    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['gmat', 'work_experience'])

    workExperience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Years experience: " + str(workExperience))
    singleSampleDf = singleSampleDf._append({'gmat':gmat,
                                            'work_experience':workExperience},
                                        ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {'choice': workExperience, 'gmat':gmat, 
                'prediction':singlePrediction})

