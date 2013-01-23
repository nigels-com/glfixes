#!/bin/sh
cd gl && \
  wget --mirror --no-parent --no-host-directories --cut-dirs=2 --accept=txt,spec,tm \
    http://www.opengl.org/registry/

