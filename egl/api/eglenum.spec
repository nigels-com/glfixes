# This is the EGL enumerant registry.
#
# It is an extremely important file. Only the Khronos API Registrar
# (currently Jon Leech) should change it.
#
# Rules for enum allocation are the same as for the OpenGL enumerant
# registry. To obtain an EGL enumerant allocation, submit a request in
# the Khronos Bugzilla for Product "EGL", component "Registry".
#
# Current version at http://www.khronos.org/registry/egl/
# $Revision: 21116 $ on $Date: 2013-04-11 03:32:10 -0700 (Thu, 11 Apr 2013) $

# EGL Versioning
Extensions define:
	VERSION_1_0					= 1
	VERSION_1_1					= 1
	VERSION_1_2					= 1
	VERSION_1_3					= 1

# EGL Enumerants.

EGLBoolean enum:
	FALSE						= 0
	TRUE						= 1

# These values may vary depending on semantics of native concepts
# DONT_CARE is an attribute value
EGLOutOfBand enum:
	DEFAULT_DISPLAY					= ((void *)0)
	NO_CONTEXT					= ((EGLContext)0)
	NO_DISPLAY					= ((EGLDisplay)0)
	NO_SURFACE					= ((EGLSurface)0)
	DONT_CARE					= ((EGLint)-1)

# Errors / GetError return values
EGLError enum:
	SUCCESS						= 0x3000
	NOT_INITIALIZED					= 0x3001
	BAD_ACCESS					= 0x3002
	BAD_ALLOC					= 0x3003
	BAD_ATTRIBUTE					= 0x3004
	BAD_CONFIG					= 0x3005
	BAD_CONTEXT					= 0x3006
	BAD_CURRENT_SURFACE				= 0x3007
	BAD_DISPLAY					= 0x3008
	BAD_MATCH					= 0x3009
	BAD_NATIVE_PIXMAP				= 0x300A
	BAD_NATIVE_WINDOW				= 0x300B
	BAD_PARAMETER					= 0x300C
	BAD_SURFACE					= 0x300D
	CONTEXT_LOST					= 0x300E
# Reserved for Graham Connor, Imagination Tech.
	CONTEXT_LOST_IMG				= 0x300E
# Khronos_future_use: 0x300F-0x301F (for additional errors)

# Config attribute names
EGLConfigAttrib enum:
	BUFFER_SIZE					= 0x3020
	ALPHA_SIZE					= 0x3021
	BLUE_SIZE					= 0x3022
	GREEN_SIZE					= 0x3023
	RED_SIZE					= 0x3024
	DEPTH_SIZE					= 0x3025
	STENCIL_SIZE					= 0x3026
	CONFIG_CAVEAT					= 0x3027
	CONFIG_ID					= 0x3028
	LEVEL						= 0x3029
	MAX_PBUFFER_HEIGHT				= 0x302A
	MAX_PBUFFER_PIXELS				= 0x302B
	MAX_PBUFFER_WIDTH				= 0x302C
	NATIVE_RENDERABLE				= 0x302D
	NATIVE_VISUAL_ID				= 0x302E
	NATIVE_VISUAL_TYPE				= 0x302F
# Added, then removed from EGL 1.3
#	PRESERVED_RESOURCES				= 0x3030
	SAMPLES						= 0x3031
	SAMPLE_BUFFERS					= 0x3032
	SURFACE_TYPE					= 0x3033
	TRANSPARENT_TYPE				= 0x3034
	TRANSPARENT_BLUE_VALUE				= 0x3035
	TRANSPARENT_GREEN_VALUE				= 0x3036
	TRANSPARENT_RED_VALUE				= 0x3037
	NONE						= 0x3038 # Attrib list terminator
	BIND_TO_TEXTURE_RGB				= 0x3039
	BIND_TO_TEXTURE_RGBA				= 0x303A
	MIN_SWAP_INTERVAL				= 0x303B
	MAX_SWAP_INTERVAL				= 0x303C
	LUMINANCE_SIZE					= 0x303D
	ALPHA_MASK_SIZE					= 0x303E
	COLOR_BUFFER_TYPE				= 0x303F
	RENDERABLE_TYPE					= 0x3040
	MATCH_NATIVE_PIXMAP				= 0x3041
	CONFORMANT					= 0x3042
# EGL_KHR_config_attribs
	CONFORMANT_KHR					= 0x3042
# EGL_KHR_lock_surface
	MATCH_FORMAT_KHR				= 0x3043

# Khronos_future_use: 0x3044-0x304F (for additional config attributes)

# Config attribute values
EGLConfigAttribValue enum:
	SLOW_CONFIG					= 0x3050 # CONFIG_CAVEAT value
	NON_CONFORMANT_CONFIG				= 0x3051 # CONFIG_CAVEAT value
	TRANSPARENT_RGB					= 0x3052 # TRANSPARENT_TYPE value
	NO_TEXTURE					= 0x305C # TEXTURE_FORMAT/TARGET value
	TEXTURE_RGB					= 0x305D # TEXTURE_FORMAT value
	TEXTURE_RGBA					= 0x305E # "
	TEXTURE_2D					= 0x305F # TEXTURE_TARGET value
	RGB_BUFFER					= 0x308E # COLOR_BUFFER_TYPE value
	LUMINANCE_BUFFER				= 0x308F # "

# Config attribute mask bits
EGLSurfaceTypeMask enum:
	PBUFFER_BIT					= 0x0001 # SURFACE_TYPE mask bit
	PIXMAP_BIT					= 0x0002 # "
	WINDOW_BIT					= 0x0004 # "
# EGL_TAO_image_surface (approximate - spec not registered yet - owned by Phil Huxley)
	PBUFFER_IMAGE_BIT_TAO				= 0x0008 # "
	PBUFFER_PALETTE_IMAGE_BIT_TAO			= 0x0010 # "
# EGL 1.3 bits
	VG_COLORSPACE_LINEAR_BIT			= 0x0020 # "
	VG_ALPHA_FORMAT_PRE_BIT				= 0x0040 # "
# EGL_KHR_config_attribs bits
	VG_COLORSPACE_LINEAR_BIT_KHR			= 0x0020 # "
	VG_ALPHA_FORMAT_PRE_BIT_KHR			= 0x0040 # "
# EGL_KHR_lock_surface bits
	LOCK_SURFACE_BIT_KHR				= 0x0080 # "
	OPTIMAL_FORMAT_BIT_KHR				= 0x0100 # "
# EGL 1.4 bits
	MULTISAMPLE_RESOLVE_BOX_BIT			= 0x0200 # "
	SWAP_BEHAVIOR_PRESERVED_BIT			= 0x0400 # "
# EGL_NV_stream_producer_eglsurface (Bug 8064)
#	EGL_STREAM_BIT_NV				= 0x0800 # "

EGLRenderableTypeMask enum:
	OPENGL_ES_BIT					= 0x0001 # RENDERABLE_TYPE mask bit
	OPENVG_BIT					= 0x0002 # "
	OPENGL_ES2_BIT					= 0x0004 # "
	OPENGL_BIT					= 0x0008 # "    # EGL 1.4
	INTEROP_BIT_KHR					= 0x0010 # "    # EGL_KHR_interop
	OPENMAX_IL_BIT_KHR				= 0x0020 # "    # EGL_KHR_interop
	OPENGL_ES3_BIT_KHR				= 0x0040 # "    # EGL_KHR_create_context rev 13

# QueryString targets
EGLQueryString enum:
	VENDOR						= 0x3053
	VERSION						= 0x3054
	EXTENSIONS					= 0x3055
	CLIENT_APIS					= 0x308D

# QuerySurface / SurfaceAttrib / CreatePbufferSurface targets
EGLSurfaceAttrib enum:
	HEIGHT						= 0x3056
	WIDTH						= 0x3057
	LARGEST_PBUFFER					= 0x3058
	TEXTURE_FORMAT					= 0x3080 # For pbuffers bound as textures
	TEXTURE_TARGET					= 0x3081 # "
	MIPMAP_TEXTURE					= 0x3082 # "
	MIPMAP_LEVEL					= 0x3083 # "
	RENDER_BUFFER					= 0x3086
	VG_COLORSPACE					= 0x3087
	COLORSPACE					= EGL_VG_COLORSPACE	    # EGL 1.3 token renaming
	VG_ALPHA_FORMAT					= 0x3088
	ALPHA_FORMAT					= VG_ALPHA_FORMAT	# EGL 1.3 token renaming
	HORIZONTAL_RESOLUTION				= 0x3090
	VERTICAL_RESOLUTION				= 0x3091
	PIXEL_ASPECT_RATIO				= 0x3092
	SWAP_BEHAVIOR					= 0x3093
	MULTISAMPLE_RESOLVE				= 0x3099 # EGL 1.4 SurfaceAttrib

# COLORSPACE surface attribute values
EGLColorspace enum:
	VG_COLORSPACE_sRGB				= 0x3089
	VG_COLORSPACE_LINEAR				= 0x308A
	COLORSPACE_sRGB					= EGL_VG_COLORSPACE_sRGB    # EGL 1.3 token renaming
	COLORSPACE_LINEAR				= EGL_VG_COLORSPACE_LINEAR  # EGL 1.3 token renaming

# ALPHA_FORMAT surface attribute values
EGLAlphaFormat enum:
	VG_ALPHA_FORMAT_NONPRE				= 0x308B
	VG_ALPHA_FORMAT_PRE				= 0x308C
	ALPHA_FORMAT_NONPRE				= VG_ALPHA_FORMAT_NONPRE # EGL 1.3 token renaming
	ALPHA_FORMAT_PRE				= VG_ALPHA_FORMAT_PRE	 # EGL 1.3 token renaming

# SWAP_BEHAVIOR surface attribute values
EGLSwapBehavior enum:
	BUFFER_PRESERVED				= 0x3094
	BUFFER_DESTROYED				= 0x3095

# Constant values related to HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION,
#   and PIXEL_ASPECT_RATIO.
# DISPLAY_SCALING is a scale factor used to represent fractional values
#   as integers.
# UNKNOWN is returned for resolution & aspect ratio of offscreen
#   surfaces.
EGLDisplayScaling enum:
	DISPLAY_SCALING					= 10000
	UNKNOWN						= ((EGLint)-1)

# CreatePbufferFromClientBuffer buffer type
EGLClientBufferType enum:
	OPENVG_IMAGE					= 0x3096

# QueryContext target
EGLQueryContextTarget enum:
	CONTEXT_CLIENT_TYPE				= 0x3097

# CreateContext attributes
EGLCreateContextAttrib enum:
	CONTEXT_CLIENT_VERSION				= 0x3098

# MULTISAMPLE_RESOLVE surface attribute values
EGLMultisampleResolve enum:
	MULTISAMPLE_RESOLVE_DEFAULT			= 0x309A # EGL 1.4
	MULTISAMPLE_RESOLVE_BOX				= 0x309B # EGL 1.4

# Khronos_future_use: 0x309C-0x309F

# BindAPI <api> target
EGLBindAPITarget enum:
	OPENGL_ES_API					= 0x30A0
	OPENVG_API					= 0x30A1
	OPENGL_API					= 0x30A2    # EGL 1.4

# Khronos_future_use: 0x30A3-0x30AF (reserved for additional client API names)

# BindTexImage / ReleaseTexImage buffer target, and
# RENDER_BUFFER surface attribute values
EGLBindBufferTarget enum:
	BACK_BUFFER					= 0x3084
	SINGLE_BUFFER					= 0x3085

# GetCurrentSurface targets
EGLSurfaceName enum:
	DRAW						= 0x3059
	READ						= 0x305A

# WaitNative engines
EGLEngine enum:
	CORE_NATIVE_ENGINE				= 0x305B

###############################################################################

# Khronos: 0x3000-0x305F (used, or marked as reserved above)

###############################################################################

# Tao: 0x3060-0x306F
# Reserved for Phil Huxley

# TAO_future_use: 0x3060-0x306F

###############################################################################

# Nokia: 0x3070-0x307F
# Reserved for Jani Vaarala

# NOK_future_use: 0x3070-0x307F (Jani Vaarala, Nokia)

###############################################################################

# Khronos: 0x3080-0x30AF (used, or marked as reserved above)

###############################################################################

# NVIDIA: 0x30B0-0x30BF
# Reserved for Ignacio Llamas

# EGL Image extension names corresponding to these enums TBD once final specs are ready
#	NATIVE_PIXMAP_KHR		      0x30B0	# eglCreateImageKHR targets
#	GL_TEXTURE_2D_KHR		      0x30B1
#	GL_TEXTURE_3D_KHR		      0x30B2
#	GL_TEXTURE_CUBE_MAP_POSITIVE_X_KHR    0x30B3
#	GL_TEXTURE_CUBE_MAP_NEGATIVE_X_KHR    0x30B4
#	GL_TEXTURE_CUBE_MAP_POSITIVE_Y_KHR    0x30B5
#	GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_KHR    0x30B6
#	GL_TEXTURE_CUBE_MAP_POSITIVE_Z_KHR    0x30B7
#	GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_KHR    0x30B8
#	GL_RENDERBUFFER_KHR		      0x30B9
#	VG_PARENT_IMAGE_KHR		      0x30BA
#	GL_TEXTURE_RECTANGLE_NV_KHR	      0x30BB
#	GL_TEXTURE_LEVEL_KHR		      0x30BC	# eglCreateImageKHR attributes
#	GL_TEXTURE_ZOFFSET_KHR		      0x30BD

# EGL_NV_post_sub_buffer
#	EGL_POST_SUB_BUFFER_SUPPORTED_NV      0x30BE

EGL_EXT_create_context_robustness enum:
	CONTEXT_OPENGL_ROBUST_ACCESS_EXT		= 0x30BF

###############################################################################

# Khronos: 0x30C0-0x30CF

EGL_KHR_lock_surface enum:
	FORMAT_RGB_565_EXACT_KHR			= 0x30C0
	FORMAT_RGB_565_KHR				= 0x30C1
	FORMAT_RGBA_8888_EXACT_KHR			= 0x30C2
	FORMAT_RGBA_8888_KHR				= 0x30C3
	MAP_PRESERVE_PIXELS_KHR				= 0x30C4
	LOCK_USAGE_HINT_KHR				= 0x30C5
	BITMAP_POINTER_KHR				= 0x30C6
	BITMAP_PITCH_KHR				= 0x30C7
	BITMAP_ORIGIN_KHR				= 0x30C8
	BITMAP_PIXEL_RED_OFFSET_KHR			= 0x30C9
	BITMAP_PIXEL_GREEN_OFFSET_KHR			= 0x30CA
	BITMAP_PIXEL_BLUE_OFFSET_KHR			= 0x30CB
	BITMAP_PIXEL_ALPHA_OFFSET_KHR			= 0x30CC
	BITMAP_PIXEL_LUMINANCE_OFFSET_KHR		= 0x30CD
	LOWER_LEFT_KHR					= 0x30CE
	UPPER_LEFT_KHR					= 0x30CF

###############################################################################

# Symbian: 0x30D0-0x30DF
# Reserved for Robert Palmer (bug #2545)

# SYM_future_use: 0x30D0-0x30D1

# EGL_KHR_image_base
	IMAGE_PRESERVED_KHR				= 0x30D2

# EGL_NOK_image_shared
	SHARED_IMAGE_NOK				= 0x30DA

# SYM_future_use: 0x30D3-0x30D9, 0x30DB-0x30DF

###############################################################################

# NVIDIA: 0x30E0-0x30EF
# Reserved for Russell Pflughaupt (bug #3314)

# EGL_NV_coverage_sample
	COVERAGE_BUFFERS_NV				= 0x30E0
	COVERAGE_SAMPLES_NV				= 0x30E1

# EGL_NV_depth_nonlinear
	DEPTH_ENCODING_NONE_NV				= 0	    # Not an alias for EGL_NONE!
	DEPTH_ENCODING_NV				= 0x30E2
	DEPTH_ENCODING_NONLINEAR_NV			= 0x30E3

# NV_future_use: 0x30E4-0x30E5

# EGL_NV_sync
	SYNC_PRIOR_COMMANDS_COMPLETE_NV			= 0x30E6
	SYNC_STATUS_NV					= 0x30E7
	SIGNALED_NV					= 0x30E8
	UNSIGNALED_NV					= 0x30E9
	ALREADY_SIGNALED_NV				= 0x30EA
	TIMEOUT_EXPIRED_NV				= 0x30EB
	CONDITION_SATISFIED_NV				= 0x30EC
	SYNC_TYPE_NV					= 0x30ED
	SYNC_CONDITION_NV				= 0x30EE
	SYNC_FENCE_NV					= 0x30EF

###############################################################################

# Khronos: 0x30F0-0x30FF

# Draft EGL_KHR_fence_sync
#	 SYNC_PRIOR_COMMANDS_COMPLETE_KHR		 = 0x30F0
#	 ALREADY_SIGNALED_KHR				 = 0x30F4
#	 SYNC_CONDITION_KHR				 = 0x30F8
#	 SYNC_FENCE_KHR					 = 0x30F9

EGL_KHR_reusable_sync enum:
	SYNC_STATUS_KHR					= 0x30F1
	SIGNALED_KHR					= 0x30F2
	UNSIGNALED_KHR					= 0x30F3
	TIMEOUT_EXPIRED_KHR				= 0x30F5
	CONDITION_SATISFIED_KHR				= 0x30F6
	SYNC_TYPE_KHR					= 0x30F7
	SYNC_REUSABLE_KHR				= 0x30FA
	SYNC_FLUSH_COMMANDS_BIT_KHR			= 0x0001    # eglClientWaitSyncKHR <flags>
	FOREVER_KHR					= 0xFFFFFFFFFFFFFFFFull
	NO_SYNC_KHR					= ((EGLSyncKHR)0)

EGL_KHR_create_context enum:
	CONTEXT_MAJOR_VERSION_KHR			= EGL_CONTEXT_CLIENT_VERSION
	CONTEXT_MINOR_VERSION_KHR			= 0x30FB
	CONTEXT_FLAGS_KHR				= 0x30FC
	CONTEXT_OPENGL_PROFILE_MASK_KHR			= 0x30FD

# Context creation flag bits - all used by EGL_KHR_create_context today
EGLContextCreationMask enum:
	CONTEXT_OPENGL_DEBUG_BIT_KHR			= 0x00000001
	CONTEXT_OPENGL_FORWARD_COMPATIBLE_BIT_KHR	= 0x00000002
	CONTEXT_OPENGL_ROBUST_ACCESS_BIT_KHR		= 0x00000004

# Profile mask bits - all used by EGL_KHR_create_context today
EGLContextProfileMask enum:
	CONTEXT_OPENGL_CORE_PROFILE_BIT_KHR		= 0x00000001
	CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT_KHR	= 0x00000002

# Khronos_future_use: 0x30FE-0x30FF

###############################################################################

# Imagination Tech.: 0x3100-0x310F
# Reserved for Ben Bowman (Khronos bug 4748)

EGL_IMG_context_priority enum:
	CONTEXT_PRIORITY_LEVEL_IMG			= 0x3100
	CONTEXT_PRIORITY_HIGH_IMG			= 0x3101
	CONTEXT_PRIORITY_MEDIUM_IMG			= 0x3102
	CONTEXT_PRIORITY_LOW_IMG			= 0x3103

# IMG_future_use: 0x3104-0x310F

###############################################################################

# Antix: 0x3110-0x311F
# Reserved for Tim Renouf (Khronos bug 4949)

EGL_KHR_lock_surface2 enum:
	BITMAP_PIXEL_SIZE_KHR				= 0x3110

# ATX_future_use: 0x3111-0x311F

###############################################################################

# AMD: 0x3120-0x312F
# Reserved for David Garcia (Khronos bug 5149)

# AMD_future_use: 0x3120-0x312F

###############################################################################

# NVIDIA: 0x3130-0x313F
# Reserved for Greg Prisament (Khronos bug 5166)

# NV_future_use: 0x3130

EGL_NV_coverage_sample_resolve enum:
	COVERAGE_SAMPLE_RESOLVE_NV			= 0x3131
	COVERAGE_SAMPLE_RESOLVE_DEFAULT_NV		= 0x3132
	COVERAGE_SAMPLE_RESOLVE_NONE_NV			= 0x3133

EGL_EXT_multiview_window enum:
	MULTIVIEW_VIEW_COUNT_EXT			= 0x3134

# NV_future_use: 0x3135

EGL_NV_3dvision_surface enum:
	EGL_AUTO_STEREO_NV				= 0x3136

# NV_future_use: 0x3137

EGL_EXT_create_context_robustness enum:
	CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_EXT	= 0x3138

# NV_future_use: 0x3139-0x313C

EGL_EXT_buffer_age enum:
	EGL_BUFFER_AGE_EXT				= 0x313D

# NV_future_use: 0x313E-0x313F

###############################################################################

# Google/Android: 0x3140-0x314F
# Reserved for Mathias Agopian (Khronos bug 5199)

EGL_ANDROID_image_native_buffer enum:
	EGL_NATIVE_BUFFER_ANDROID			= 0x3140

# Google_future_use: 0x3141

EGL_ANDROID_recordable enum:
	EGL_RECORDABLE_ANDROID				= 0x3142

# Google_future_use: 0x3143

EGL_ANDROID_native_fence_sync enum:
	EGL_SYNC_NATIVE_FENCE_ANDROID			= 0x3144
	EGL_SYNC_NATIVE_FENCE_FD_ANDROID		= 0x3145
	EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID		= 0x3146
	EGL_NO_NATIVE_FENCE_FD_ANDROID			= -1

EGL_ANDROID_framebuffer_target enum:
	EGL_FRAMEBUFFER_TARGET_ANDROID			= 0x3147

# Google_future_use: 0x3148-0x314F

###############################################################################

# Nokia: 0x3150-0x315F
# Reserved for Robert Palmer (Khronos bug 5368)

# NOK_future_use: 0x3150-0x315F

###############################################################################

# Seaweed: 0x3160-0x316F
# Reserved for Sree Sridharan (Khronos public bug 198)

# SEAWEED_future_use: 0x3160-0x316F

###############################################################################

# QNX: 0x3170-0x318F
# Reserved for Joel Pilon (Khronos bug 5834)

# QNX_future_use: 0x3170-0x318F

###############################################################################

# FSL: 0x3190-0x31AF
# Reserved for Brian Murray (Khronos bug 5939)

# FSL_future_use: 0x3190-0x31AF

###############################################################################

# Khronos: 0x31B0-0x31BF
# Reserved for Marcus Lorentzon (Khronos bug 6437)

# EGL image stream (assignments TBD): 0x31B0-0x31BC

EGL_KHR_create_context enum: (additional; see above)
	CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_KHR	= 0x31BD
	NO_RESET_NOTIFICATION_KHR			= 0x31BE
	LOSE_CONTEXT_ON_RESET_KHR			= 0x31BF

EGL_EXT_create_context_robustness enum:
	NO_RESET_NOTIFICATION_EXT			= 0x31BE
	LOSE_CONTEXT_ON_RESET_EXT			= 0x31BF

###############################################################################

# Qualcomm: 0x31C0-0x31CF
# Reserved for Maurice Ribble (Khronos bug 6644)

# QCOM_future_use: 0x31C0-0x31CF

###############################################################################

# Mesa: 0x31D0-0x31DF
# Reserved for Kristian Høgsberg (Khronos bug 6757)

MESA_drm_image enum:
	DRM_BUFFER_FORMAT_MESA				= 0x31D0
	DRM_BUFFER_USE_MESA				= 0x31D1
	DRM_BUFFER_FORMAT_ARGB32_MESA			= 0x31D2
	DRM_BUFFER_MESA					= 0x31D3
	DRM_BUFFER_STRIDE_MESA				= 0x31D4
# EGL_DRM_BUFFER_USE_MESA bits
	DRM_BUFFER_USE_SCANOUT_MESA			= 0x00000001
	DRM_BUFFER_USE_SHARE_MESA			= 0x00000002

# MESA_future_use: 0x31D5-0x31DF

###############################################################################

# HI Corp: 0x31E0-0x31EF
# Reserved for Mark Callow (Khronos bug 6799)

# HI_future_use: 0x31E0-0x31EF

###############################################################################

# Khronos: 0x31F0-0x31FF

# Draft EGL_KHR_image_uses family of extensions

# Draft KHR_image_use_gl1_renderbuffer enum:
#	IMAGE_USE_AS_OPENGL_ES1_RENDERBUFFER_KHR	 = 0x31F0

# Draft KHR_image_use_gl1_texture_2d enum:
#	IMAGE_USE_AS_OPENGL_ES1_TEXTURE_2D_KHR		 = 0x31F1

# Draft KHR_image_use_gl1_texture_external enum:
#	IMAGE_USE_AS_OPENGL_ES1_TEXTURE_EXTERNAL_KHR	 = 0x31F2

# Draft KHR_image_use_gl2_renderbuffer enum:
#	IMAGE_USE_AS_OPENGL_ES2_RENDERBUFFER_KHR	 = 0x31F3

# Draft KHR_image_use_gl2_texture_2d enum:
#	IMAGE_USE_AS_OPENGL_ES2_TEXTURE_2D_KHR		 = 0x31F4

# Draft KHR_image_use_gl2_texture_external enum:
#	IMAGE_USE_AS_OPENGL_ES2_TEXTURE_EXTERNAL_KHR	 = 0x31F5

# Draft KHR_image_use_vg_vgimage enum:
#	IMAGE_USE_AS_OPENVG_IMAGE_KHR			 = 0x31F6

# EGL_MESA_image_stream_internal enum:
#	STREAM_CONSUMER_ATTACHMENT_MESA			 = 0x31F7
#	NO_FORMAT_MESA					 = 0x31F8
#	FORMAT_RGBA8888_MESA				 = 0x31F9
#	FORMAT_RGB888_MESA				 = 0x31FA
#	FORMAT_RGB565_MESA				 = 0x31FB

EGL_KHR_stream_fifo
	EGL_STREAM_FIFO_LENGTH_KHR			= 0x31FC
	EGL_STREAM_TIME_NOW_KHR				= 0x31FD
	EGL_STREAM_TIME_CONSUMER_KHR			= 0x31FE
	EGL_STREAM_TIME_PRODUCER_KHR			= 0x31FF

###############################################################################

# ANGLE Project: 0x3200-0x320F
# Reserved for Daniel Koch (Khronos bug 7139)

EGL_ANGLE_surface_d3d_texture_2d_share_handle enum:
	D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE		= 0x3200

EGL_ANGLE_d3d_share_handle_client_buffer enum:
	reuse EGL_ANGLE_surface_d3d_texture_2d_share_handle D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE

# ANGLE_future_use: 0x3201-0x320F

###############################################################################

# Khronos: 0x3210-0x321F

EGL_KHR_stream enum:
	EGL_CONSUMER_LATENCY_USEC_KHR			= 0x3210
	EGL_PRODUCER_FRAME_KHR				= 0x3212
	EGL_CONSUMER_FRAME_KHR				= 0x3213
	EGL_STREAM_STATE_KHR				= 0x3214
	EGL_STREAM_STATE_CREATED_KHR			= 0x3215
	EGL_STREAM_STATE_CONNECTING_KHR			= 0x3216
	EGL_STREAM_STATE_EMPTY_KHR			= 0x3217
	EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR	= 0x3218
	EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR	= 0x3219
	EGL_STREAM_STATE_DISCONNECTED_KHR		= 0x321A
	EGL_BAD_STREAM_KHR				= 0x321B
	EGL_BAD_STATE_KHR				= 0x321C

EGL_NV_stream_producer_eglsurface enum:
	EGL_BUFFER_COUNT_NV				= 0x321D

EGL_NV_stream_consumer_gltexture enum:
	EGL_CONSUMER_ACQUIRE_TIMEOUT_USEC_NV		= 0x321E

EGL_NV_stream_sync enum:
	EGL_SYNC_NEW_FRAME_NV				= 0x321F

# Khronos_future_use: 0x3211

###############################################################################

# NVIDIA: 0x3220-0x325F
# Reserved for Greg Roth (Bug 8220)

###############################################################################

# Broadcom: 0x3260-0x326F
# Reserved for Gary Sweet (Public bug 620)

###############################################################################

# ARM: 0x3270-0x328F
# Reserved for Tom Cooksey (Bug 9963)

EGL_EXT_image_dma_buf_import enum:
	EGL_LINUX_DMA_BUF_EXT				= 0x3270
	EGL_LINUX_DRM_FOURCC_EXT			= 0x3271
	EGL_DMA_BUF_PLANE0_FD_EXT			= 0x3272
	EGL_DMA_BUF_PLANE0_OFFSET_EXT			= 0x3273
	EGL_DMA_BUF_PLANE0_PITCH_EXT			= 0x3274
	EGL_DMA_BUF_PLANE1_FD_EXT			= 0x3275
	EGL_DMA_BUF_PLANE1_OFFSET_EXT			= 0x3276
	EGL_DMA_BUF_PLANE1_PITCH_EXT			= 0x3277
	EGL_DMA_BUF_PLANE2_FD_EXT			= 0x3278
	EGL_DMA_BUF_PLANE2_OFFSET_EXT			= 0x3279
	EGL_DMA_BUF_PLANE2_PITCH_EXT			= 0x327A
	EGL_YUV_COLOR_SPACE_HINT_EXT			= 0x327B
	EGL_SAMPLE_RANGE_HINT_EXT			= 0x327C
	EGL_YUV_CHROMA_HORIZONTAL_SITING_HINT_EXT	= 0x327D
	EGL_YUV_CHROMA_VERTICAL_SITING_HINT_EXT		= 0x327E
	EGL_ITU_REC601_EXT				= 0x327F
	EGL_ITU_REC709_EXT				= 0x3280
	EGL_ITU_REC2020_EXT				= 0x3281
	EGL_YUV_FULL_RANGE_EXT				= 0x3282
	EGL_YUV_NARROW_RANGE_EXT			= 0x3283
	EGL_YUV_CHROMA_SITING_0_EXT			= 0x3284
	EGL_YUV_CHROMA_SITING_0_5_EXT			= 0x3285

EGL_ARM_pixmap_multisample_discard enum:
	EGL_DISCARD_SAMPLES_ARM				= 0x3286

###############################################################################

# Mesa: 0x3290-0x329F
# Reserved for John Kåre Alsaker (Public bug 757)

###############################################################################
### Please remember that new EGL enum allocations must be obtained by request
### to the Khronos API Registrar (see comments at the top of this file).
### File requests in the Khronos Bugzilla, Product "EGL", Component "Registry"
###############################################################################

# Any_vendor_future_use: 0x32A0-0x3FFF
#
#   This range must be the last range in the file.  To generate a new
#   range, allocate multiples of 16 from the beginning of the
#   Any_vendor_future_use range and update eglenum.spec.
