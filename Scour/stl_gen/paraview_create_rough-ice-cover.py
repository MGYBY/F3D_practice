# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

num_box_y = 4
num_box_x = 12
num_box_tot = num_box_x*num_box_y
box_xlen = 0.75
box_ylen = 0.75
box_zlen = 0.75

box_xStart = 1.125
box_yStart = 13.0/6.0
box_xSpacing = 2.25
box_ySpacing = 13.0/6.0
offset_sed = 3.0
box_zCoord = 15.0183-box_zlen/2.0+offset_sed

cone_d = 2.25
cone_h = 2.25
box_xStart = 0.0+0.5*cone_d
box_yStart = 0.0+0.5*cone_d
cone_top = 15.0183

for iboxx in range(num_box_x):
    for iboxy in range(num_box_y):
        box_str = "Cone"+str(num_box_tot+1)

        # create a new 'Cone'
        cone1 = Cone(registrationName=box_str)

        # Properties modified on cone1
        cone1.Resolution = 80
        cone1.Radius = cone_d/2.0
        cone1.Height = cone_h
        cone1.Center = [box_xStart+cone_d*iboxx, box_yStart+cone_d*iboxy, cone_top-0.5*cone_h]
        cone1.Direction = [0.0, 0.0, -1.0]

        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')

        # show data in view
        box1Display = Show(cone1, renderView1, 'GeometryRepresentation')

        # trace defaults for the display properties.
        box1Display.Representation = 'Surface'

        # reset view to fit data
        renderView1.ResetCamera(False, 0.9)

        # get the material library
        materialLibrary1 = GetMaterialLibrary()

        # update the view to ensure updated data information
        renderView1.Update()

        #================================================================
        # addendum: following script captures some of the application
        # state to faithfully reproduce the visualization during playback
        #================================================================

        # get layout
        layout1 = GetLayout()

        #--------------------------------
        # saving layout sizes for layouts

        # layout/tab size in pixels
        layout1.SetSize(1596, 794)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
renderView1.CameraPosition = [1.5, 2.541670083999634, 17.902848967670945]
renderView1.CameraFocalPoint = [1.5, 2.541670083999634, 15.39330005645752]
renderView1.CameraParallelScale = 0.649519052838329


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
