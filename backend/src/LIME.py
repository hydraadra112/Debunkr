from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import make_pipeline

class LIMEInterpreter:
    def __init__(self, vectorizer, model, class_names=[0,1]): # 0=real news, 1=fake news
        self.pipeline = make_pipeline(vectorizer, model)
        self.class_names = class_names
        self.explainer = LimeTextExplainer(class_names=self.class_names)

    def explain(self, text, num_features=10):
        """
        Generate LIME explanation and return a dict of word:score AND the probability of class pred
        """
        explanation = self.explainer.explain_instance(
            text_instance=text,
            classifier_fn=self.pipeline.predict_proba,
            num_features=num_features,
            num_samples=1000
        )
        
        # Convert to dict
        word_scores = {str(word): round(score, 5) for word, score in explanation.as_list()}
        return word_scores, round(explanation.predict_proba.max() * 100, 2)
    

    # Visualize function to only download LIME but optional for now
    # Only apply it if we have more time
    # def visualize(self, text, num_features=10):
    #     """
    #     Launch HTML visualization in browser.
    #     """
    #     explanation = self.explainer.explain_instance(
    #         text_instance=text,
    #         classifier_fn=self.pipeline.predict_proba,
    #         num_features=num_features
    #     )
    #     explanation.show_in_notebook()  # Or explanation.save_to_file("lime_explanation.html")
