#!/bin/sh

#
# Extension specifications, .spec and .tm files
#

wget -P gl --mirror --no-parent --no-host-directories --cut-dirs=1 --accept=txt,spec,tm,h \
  http://www.opengl.org/registry/

#
# OpenGL Software Development Kit - manual pages for GL and GLSL
#

wget -P gl --mirror --no-parent --no-host-directories --cut-dirs=1 --accept=html,xml \
  http://www.opengl.org/sdk/docs/man4/xhtml/

wget -P gl --mirror --no-parent --no-host-directories --cut-dirs=1 --accept=html,xml \
  http://www.opengl.org/sdk/docs/manglsl/xhtml/
