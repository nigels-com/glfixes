#!/bin/sh

#
# Extension specifications, .spec and .tm files
#

wget -P gl --mirror --no-parent --no-host-directories --cut-dirs=2 --accept=txt,spec,tm \
  http://www.opengl.org/registry/

#
# OpenGL Software Development Kit - manual pages
#

wget -P gl --mirror --no-parent --no-host-directories --cut-dirs=1 --accept=html,xml \
  http://www.opengl.org/sdk/docs/man4/xhtml/
