from bisect import bisect
from re import A
from xmlrpc.client import Boolean
import vtk
import slicer
import bisect

class PoseInterpolation:
  """Create interpolated camera poses along the curve points.
  """

  def __init__(self, curveNode, controlPointOrientations, resampledPath, pathPedigreeIds):
    """
      :param curveNode: node object representing the guide curve.
      :param controlPointOrientations: orientations at control points that are to be interpolated.
      :param resampledPath: path points constructed by resampling along the curve.
      :param pathPedigreeIds: pedigree Ids for the resampled points.
    """

    # Get Control point to curve point index mapping:
    controlPointPedigree = []
    for cpId in range(len(controlPointOrientations)):
        controlPointPedigree.append(curveNode.GetCurvePointIndexFromControlPointIndex(cpId))

    # Iterate over each path point, and interpolate orientation:
    # currentControlPointId = 0
    for pId in len(resampledPath):
      pathPoint = resampledPath[pId]
      pedigreeId = pathPedigreeIds[pId]
      cpId1 = bisect.bisect_right(controlPointPedigree, pedigreeId)
      if cpId1 > 0:
        cpId0 = cpId1 - 1
        controlPointPedigree[cpId0]
