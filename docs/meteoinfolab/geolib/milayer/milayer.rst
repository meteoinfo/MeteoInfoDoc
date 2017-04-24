.. _docs-meteoinfolab-geolib-milayer-MILayer:


*********************************
MILayer
*********************************

.. currentmodule:: mipylib.geolib.milayer

.. class:: MILayer

    Map layer
    
    :param layer: (*MapLayer*) MapLayer object.
    :param shapetype: (*ShapeTypes*) Shape type ['point' | 'line' | 'polygon']
    
    .. method:: cellvalue(self, fieldname, shapeindex)
    
        Get attribute table cell value.
        
        :param fieldname: (*string*) Field name.
        :param shapeindex: (*int*) Shape index.
        
        :returns: The value in attribute table identified by field name and shape index.
        
    .. method:: setcellvalue(self, fieldname, shapeindex, value)
    
        Set cell value in attribute table.
        
        :param fieldname: (*string*) Field name.
        :param shapeindex: (*int*) Shape index.
        :param value: (*object*) Cell value to be asigned.