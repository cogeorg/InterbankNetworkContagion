#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2012 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""


#-------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	sys.path.append('src/')
	from tests import Tests
	
	#
	# VARIABLES
	#
	tests = Tests()
	
	#
	# CODE
	#
	# for each appropriate chunk of the original code we need one test to ensure it is working
	args=['./br-make_tests.py',  "environments/", "test3",  "log/",  "measurements/"]
	#args = sys.argv

	#tests.bank__initialize_standard_bank(args)
	#tests.bank__update_maturity(args)
	#tests.bank__update_risk_aversion(args)         #tricky one, doesnt work yet 
	#tests.bank__get_interest(args)
	#tests.bank__liquidate_due_transactions(args)
	#tests.bank__get_new_deposits(args)
	#tests.bank__transfer_required_deposits(args)
	#tests.bank__reduce_banking_capital(args)
	#tests.bank__check_solvency(args)                
	#tests.bank__check_liquidity(args)
	#tests.bank__calculate_liquidity_demand(args)
	#tests.bank__get_central_bank_liquidity(args)
	tests.bank__liquidate_assets(args)
	#tests.bank__transfer_investments(args)                 # several unclear things, leave open first
	#tests.bank__transfer_excess_reserves(args)
	#tests.bank__calculate_optimal_investment_volume(args)  # works but maybe bug? --> see faq
	#tests.bank__initialize_transactions(args)               # parameter werden nicht übernommen. Division Error weil Transactions = 0.0
	
	#tests.updater__updater(args)
	#tests.updater__updater1(args)
	
	#tests.network__do_interbank_trades(args)
	#tests.network__remove_inactive_bank(args)
	
	#tests.test_fire_sales(args)
	
	#tests.test_state(args)
	
	#tests.updater__liquidate_assets(args)
	
	#tests.bank__test1(args)
	
