from django.db import models


class Term(models.Model):
    term_value = models.CharField(max_length=150)
    definition = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.term_value

    def to_dict_recursive(self):
        result = {
            'id': self.id,
            'topic': f"{self.term_value} - {self.definition}",
            'direction': 'down',
            'children': [],
        }

        children = Term.objects.filter(parent=self)
        for child in children:
            result['children'].append(child.to_dict_recursive())

        return result
