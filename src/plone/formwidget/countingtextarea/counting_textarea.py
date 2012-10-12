import zope.component
import zope.interface
import zope.schema.interfaces

from zope.schema.fieldproperty import FieldProperty

from z3c.form import interfaces
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget

class ICountingTextAreaWidget(interfaces.ITextAreaWidget):
    pass

class CountingTextAreaWidget(widget.HTMLTextAreaWidget, Widget):
    zope.interface.implementsOnly(ICountingTextAreaWidget)

    klass = u'textarea-widget'
    value = u''

    def update(self):
        super(CountingTextAreaWidget, self).update()
        widget.addFieldClass(self)


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def CountingTextAreaFieldWidget(field, request):
    return FieldWidget(field, CountingTextAreaWidget(request))
