"""
Buzzword tool from    
    https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
"""
import random

buzz = ('continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops', 'micro services', 'serverless',
    'high-scale')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end', 'auto-scaling', )
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously', 'rapidly', 'autonomously', 'magicaly')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts', 'delivers'
    'integrates', 'deploys', 'reduces')

def sample(l, n=1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print generate_buzz()
