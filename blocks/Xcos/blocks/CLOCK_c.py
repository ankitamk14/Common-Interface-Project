from blocks.CLKOUT_f import CLKOUT_f
from blocks.EVTDLY_c import EVTDLY_c
from blocks.SplitBlock import SplitBlock
from common.AAAAAA import *

def CLOCK_c(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLOCK_c'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'csuper', 'DEFAULT',
                         func_name, BLOCKTYPE_H)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)
    addTypeNode(outnode, TYPE_DOUBLE, AS_REAL_PARAM, 0,
                [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_INT_PARAM, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_OBJ_PARAM, parameters)
    array = ['0']
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NBZERO, 1, array)
    addPrecisionNode(outnode, TYPE_INTEGER, AS_NMODE, 1, array)
    addTypeNode(outnode, TYPE_DOUBLE, AS_STATE, 0, [])
    addTypeNode(outnode, TYPE_DOUBLE, AS_DSTATE, 0, [])
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_ODSTATE, parameters)
    addObjNode(outnode, TYPE_ARRAY, CLASS_LIST, AS_EQUATIONS, parameters)
    addgeometryNode(outnode, GEOMETRY, geometry['height'],
                    geometry['width'], geometry['x'], geometry['y'])

    # Create the SuperBlockDiagram element
    SuperBlockDiagram = addSuperNode(outnode, TYPE_SUPER,
                                     a="child",
                                     background="-1",
                                     gridEnabled="1",
                                     title="")

    Array = addSuperBlkNode(SuperBlockDiagram, TYPE_ARRAY,
                            a="context",
                            scilabClass="String[]")
    superAddNode(Array, TYPE_ADD, value="")

    mxGraphModel = addmxGraphModelNode(SuperBlockDiagram,
                                       TYPE_MODEL, a="model")
    root = addNode(mxGraphModel, TYPE_ROOT)
    addmxCellNode(root, TYPE_MXCELL,
                  id="128c18ea:1383ab8277d:-748d", a='')
    addmxCellNode(root, TYPE_MXCELL,
                  id="128c18ea:1383ab8277d:-748d",
                  parent="128c18ea:1383ab8277d:-748d", a='')

    # Create the EventOutBlock node inside the root tag
    CLKOUT_f(root, attribid, ordering, geometry, parameters)

    addPort(root, TYPE_CNTRL, id="-63efee48:189fd5ed04e:-73dd",
            parent="-73e75f0:167968eb73f:-7955", ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")

    EVTDLY_c(root, attribid, ordering, geometry, parameters)

    addPort(root, TYPE_CNTRL, id="-63efee48:189fd5ed04e:-73db",
            parent="-73e75f0:167968eb73f:-7953", ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")
    addPort(root, TYPE_CMD, id="-63efee48:189fd5ed04e:-73da",
            parent="-73e75f0:167968eb73f:-7953", ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="CommandPort", value="")

    SplitBlock(root, attribid, ordering, geometry)

    addPort(root, TYPE_CNTRL, id="-63efee48:189fd5ed04e:-73d8",
            parent="-73e75f0:167968eb73f:-7950", ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="0.0",
            style="ControlPort", value="")
    addPort(root, TYPE_CMD, id="-63efee48:189fd5ed04e:-73d7",
            parent="-73e75f0:167968eb73f:-7950", ordering="1",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="-1.0",
            style="CommandPort", value="")
    addPort(root, TYPE_CMD, id="-63efee48:189fd5ed04e:-73d6",
            parent="-73e75f0:167968eb73f:-7950", ordering="2",
            dataType="REAL_MATRIX", dataColumns="1",
            dataLines="-1", initialState="-1.0",
            style="CommandPort", value="")

    CCLink = addLink(root, TYPE_LINK, id="-63efee48:189fd5ed04e:-73d5",
                     parent="128c18ea:1383ab8277e:-748d",
                     source="-63efee48:189fd5ed04e:-73d6",
                     target="-63efee48:189fd5ed04e:-73db",
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="sourcePoint", x="0.0", y="11.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint',
                 x="100.70999999999998", y="40.0")
    addPointNode(ArrayNode, 'mxPoint', x="60.0",
                 y="40.0")
    addmxPointNode(gemotryNode, 'mxPoint',
                   a="targetPoint", x="20.0", y="-4.0")
    CCLink = addLink(root, TYPE_LINK, id="-63efee48:189fd5ed04e:-73d4",
                     parent="128c18ea:1383ab8277e:-748d",
                     source="-63efee48:189fd5ed04e:-73d7",
                     target="-63efee48:189fd5ed04e:-73dd",
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="0.0", y="11.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="10.0", y="-4.0")
    CCLink = addLink(root, TYPE_LINK, id="-63efee48:189fd5ed04e:-73d3",
                     parent="128c18ea:1383ab8277e:-748d",
                     source="-63efee48:189fd5ed04e:-73da",
                     target="-63efee48:189fd5ed04e:-73d8",
                     style="CommandControlLink", value="")
    gemotryNode = addGeoNode(CCLink, GEOMETRY, a="geometry")
    addmxPointNode(gemotryNode, 'mxPoint', a="sourcePoint",
                   x="20.0", y="44.0")
    ArrayNode = addArray(gemotryNode, TYPE_ARRAY, a="points")
    addPointNode(ArrayNode, 'mxPoint', x="60.0", y="170.0")
    addmxPointNode(gemotryNode, 'mxPoint', a="targetPoint",
                   x="0.0", y="-4.0")
    addmxCellNode(SuperBlockDiagram, TYPE_MXCELL,
                  id="128c18ea:1383ab8277d:-748d",
                  parent="128c18ea:1383ab8277d:-748d",
                  a="defaultParent")

    return outnode


def get_from_CLOCK_c(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
