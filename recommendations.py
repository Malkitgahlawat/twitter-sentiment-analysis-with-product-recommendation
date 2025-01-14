class RecommendationEngine:
    def recommend(self, sentiment, emotions):

        recommendations = {
            'positive': {
                'joy': "Try our premium features for an enhanced experience!",
                'love': "Check out our loyalty program for exclusive rewards.",
                'surprise': "Discover new deals and offers just for you!"
            },
            'negative': {
                'anger': "We apologize for the inconvenience. Contact support for help.",
                'sadness': "We’re here to improve. Tell us how we can do better.",
                'fear': "Check our FAQs to address your concerns."
            },
            'neutral': {
                'none': "Stay tuned for updates and new features!"
            }
        }

        if sentiment in recommendations:
            for emotion in emotions:
                if emotion in recommendations[sentiment]:
                    return recommendations[sentiment][emotion]
        return "Thank you for your feedback!"
