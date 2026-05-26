# ==============================================================================
# PROJECT: PHOENIX MASTER LOGIC v6.0 - ENTERPRISE BORSOD FRAMEWORK
# MODULE:  CORE_TIME_GATE
# CODENAME: VAS R 800 / BORSODI TABORNOK
# OPERATOR: DON MÉRÖK (The Brain)
# ==============================================================================
# [HU] LEÍRÁS:
# Időkapu modul az automatizált végrehajtáshoz és piaci ablakok kezeléséhez.
#
# [EN] DESCRIPTION:
# Time gate module for automated execution and market window management.
# ==============================================================================

import datetime

class TimeGate:
    def check_market_window(self):
        # [HU] Piaci ablak ellenőrzése / [EN] Validate market window
        current_time = datetime.datetime.now().time()
        if current_time >= datetime.time(9, 0) and current_time <= datetime.time(17, 0):
            return True
        return False
