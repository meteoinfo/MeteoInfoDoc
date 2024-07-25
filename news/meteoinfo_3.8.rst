.. _news-meteoinfo_3.8:


******************************************
MeteoInfo 3.8 was released (2024-3-11)
******************************************

  - New MapPlot rendering functions without MapView
  - Support LaTeX in 3D axes
  - Support unicode text in colorbar
  - Enable system error output in console
  - Support read MATLAB data file
  - Support read and write npy/npz data file
  - Support colorful streamline in 2D plot
  - Support output GeoJSON file
  - Update `gifaddframe` function to support add an BufferedImage
  - Support visible light data with calibration in AWX
  - Support `extend` and `extendfrac` parameters in contourf function
  - Add `spacing` function
  - Add `Line2D` class in plotlib package
  - Add LinearAlgebra abstract class for BLAS engine switch
  - Add render2d module
  - Format NDArray iter behaviours and add `nditer` class
  - Update MDFS data reading function for string station ID
  - Update FlatLaf to version 3.4
  - Update jackson to version 2.15.1
  - Some other bugs fixed

**Read and plot MATLAB data file**::

    fn = 'D:/Temp/matlab/lizard.mat'
    mat_data = np.loadmat(fn)
    data = mat_data['data']
    data = np.transpose(data, [1,2,0])

    axes3d(aspect='equal', orthographic=False, axes_zoom=True)
    volumeplot(data, cmap='matlab_jet', ray_casting='specular', vmin=40,
        brightness=1.5)

.. image:: ../_static/loadmat_lizard.png
