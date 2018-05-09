from rest_framework import serializers
from questions.models import Answers, Questions, UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name','last_name')



class AnswerSerializer(serializers.ModelSerializer):
    answered_by = UserModelSerializer()

    class Meta:
        model = Answers
        fields = ('id','answer','answered_by')
        depth = 1

    def to_representation(self, instance):
        """Here we Implemented filtering questions,
        if we passed allow context variable it will pass all answers.
         otherwise filters answers answered by the user"""

        ret = {}
        if self.context['allow'] == 'True':
            ret = super(AnswerSerializer, self).to_representation(instance)
        else:
            if self.context['user'] !=  instance.answered_by.id:
                ret = super(AnswerSerializer,self).to_representation(instance)
        return ret



class QuestionSerializer(serializers.ModelSerializer):
    asked_by = UserModelSerializer()
    question_answers = AnswerSerializer(many=True)

    class Meta:
        model = Questions
        depth = 1
        fields = ('id', 'question','question_answers','asked_by')



