.. docs-meteoinfo-desktop-map_layout-mask_out:


************************
Mask Out
************************

Mask layer could be set to avoid drawing graphic outside the mask extent. Set ‘SetMaskLayer’ 
to ‘True’, and then select a mask layer from ‘MaskLayer’ list. But firstly you have to have 
at least one mask layer in ‘Layers’ list. Only polygon layer could be used as mask layer. 
‘china.shp’ file in ‘Map’ folder under the software installation path can be used. Open it, 
and then select it in ‘MaskLayer’ list. Don’t use very complex polygon layer as mask layer, 
it will slow down the software obviously.

.. image:: ../../../_static/meteoinfo/maskout_before.png

.. image:: ../../../_static/meteoinfo/maskout_after.png