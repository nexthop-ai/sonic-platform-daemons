#!/usr/bin/env python3

"""
    cpo_cmis_manager_task
    CMIS management task for co-packaged optics (CPO) modules.

    Reuses the full CMIS state machine from CmisManagerTask. The set of CPO ports
    this task manages is supplied at construction via sfp_obj_dict (the same
    mechanism the base task uses), so partitioning between CPO and non-CPO ports
    happens by which objects each task is given. The only CPO-specific seam
    overridden here is how the xcvr API is obtained from the transceiver object.
"""

try:
    from .cmis_manager_task import CmisManagerTask
except ImportError as e:
    raise ImportError(str(e) + " - required module not found")


class CpoCmisManagerTask(CmisManagerTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "CpoCmisManagerTask"

    def _get_api(self, xcvr):
        # A CPO object exposes its CMIS API via get_api() (returning a CpoApi, which
        # is a CmisApi), rather than SfpBase.get_xcvr_api().
        return xcvr.get_api()
