from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def index():
	return render_template('home.html')



@app.route('/tax', methods=['GET', 'POST'])
def tax():

	if request.method == "POST":
		type = request.values.get("type")
		if type == "single":
			income = int(request.values.get("self"))
			if income <= 85200:
				mpf = 0
			else:
				mpf = (income*0.05)
				if mpf > 18000:
					mpf = 18000
			allowance = 132000
			net_charge_income = income - mpf - allowance
			net_charge_income_standard = income - mpf 
			if net_charge_income < 0:
				net_charge_income = 0
			if net_charge_income <= 50000:
				tax = int(net_charge_income*0.02)
			elif net_charge_income <= 100000:
				tax = int((net_charge_income-50000)*0.06+1000)
			elif net_charge_income <= 150000:
				tax = int((net_charge_income-100000)*0.1+1000+3000)
			elif net_charge_income <= 200000:
				tax = int((net_charge_income-150000)*0.14+1000+3000+5000)
			elif net_charge_income > 200000:
				tax = int((net_charge_income-200000)*0.17+1000+3000+5000+7000)
			standard_tax = int(net_charge_income_standard*0.15)
			if tax <= standard_tax:
				taxpay = tax
			else:
				taxpay = standard_tax
			return render_template('single.html',income = income, mpf = mpf, allowance = allowance, net_charge_income = net_charge_income, taxpay = taxpay )
		elif type == "married":
			self_income = int(request.values.get("self"))
			if self_income <= 85200:
				self_mpf = 0
			else:
				self_mpf = (self_income*0.05)
				if self_mpf > 18000:
					self_mpf = 18000
			allowance = 132000
			self_net_charge_income = self_income - self_mpf - allowance
			self_net_charge_income_standard = self_income - self_mpf
			if self_net_charge_income < 0:
				self_net_charge_income = 0
			if self_net_charge_income <= 50000:
				self_tax = int(self_net_charge_income*0.02)
			elif self_net_charge_income <= 100000:
				self_tax = int((self_net_charge_income-50000)*0.06+1000)
			elif self_net_charge_income <= 150000:
				self_tax = int((self_net_charge_income-100000)*0.1+1000+3000)
			elif self_net_charge_income <= 200000:
				self_tax = int((self_net_charge_income-150000)*0.14+1000+3000+5000)
			elif self_net_charge_income > 200000:
				self_tax = int((self_net_charge_income-200000)*0.17+1000+3000+5000+7000)
			self_standard_tax = int(self_net_charge_income_standard*0.15)
			if self_tax <= self_standard_tax:
				self_taxpay = self_tax
			else:
				self_taxpay = self_standard_tax

			spouse_income = int(request.values.get("spouse"))
			spouse_mpf = int(spouse_income*0.05)
			if spouse_income <= 85200:
				spouse_mpf = 0
			else:
				spouse_mpf = (spouse_income*0.05)
				if spouse_mpf > 18000:
					spouse_mpf = 18000
			spouse_net_charge_income = spouse_income - spouse_mpf - allowance
			spouse_net_charge_income_standard = spouse_income - spouse_mpf 
			if spouse_net_charge_income < 0:
				spouse_net_charge_income = 0
			if spouse_net_charge_income <= 50000:
				spouse_tax = int(spouse_net_charge_income*0.02)
			elif spouse_net_charge_income <= 100000:
				spouse_tax = int((spouse_net_charge_income-50000)*0.06+1000)
			elif spouse_net_charge_income <= 150000:
				spouse_tax = int((spouse_net_charge_income-100000)*0.1+1000+3000)
			elif spouse_net_charge_income <= 200000:
				spouse_tax = int((spouse_net_charge_income-150000)*0.14+1000+3000+5000)
			elif spouse_net_charge_income > 200000:
				spouse_tax = int((spouse_net_charge_income-200000)*0.17+1000+3000+5000+7000)
			spouse_standard_tax = int(spouse_net_charge_income_standard*0.15)
			if spouse_tax <= spouse_standard_tax:
				spouse_taxpay = spouse_tax
			else:
				spouse_taxpay = spouse_standard_tax
			
			joint_income = self_income + spouse_income
			joint_mpf = self_mpf + spouse_mpf
	
			joint_allowance = allowance*2
			joint_net_charge_income = joint_income - joint_mpf - joint_allowance
			joint_net_charge_income_standard = joint_income - joint_mpf
			if joint_net_charge_income < 0:
				joint_net_charge_income = 0
			if joint_net_charge_income <= 50000:
				joint_tax = int(joint_net_charge_income*0.02)
			elif joint_net_charge_income <= 100000:
				joint_tax = int((joint_net_charge_income-50000)*0.06+1000)
			elif joint_net_charge_income <= 150000:
				joint_tax = int((joint_net_charge_income-100000)*0.1+1000+3000)
			elif joint_net_charge_income <= 200000:
				joint_tax = int((joint_net_charge_income-150000)*0.14+1000+3000+5000)
			elif joint_net_charge_income > 200000:
				joint_tax = int((joint_net_charge_income-200000)*0.17+1000+3000+5000+7000)
			joint_standard_tax = int(joint_net_charge_income_standard*0.15)
			if joint_tax <= joint_standard_tax:
				joint_taxpay = joint_tax
			else:
				joint_taxpay = joint_standard_tax

			if joint_taxpay >= (self_taxpay + spouse_taxpay):
				totaltax = self_taxpay + spouse_taxpay
				return render_template('married.html',self_income = self_income, self_mpf = self_mpf, allowance = allowance, self_net_charge_income = self_net_charge_income, self_taxpay = self_taxpay, spouse_income = spouse_income, spouse_mpf = spouse_mpf, spouse_net_charge_income = spouse_net_charge_income, spouse_taxpay = spouse_taxpay, totaltax = totaltax, joint_income = joint_income, joint_mpf = joint_mpf, joint_allowance = joint_allowance, joint_net_charge_income = joint_net_charge_income, joint_taxpay = joint_taxpay)
			else:
				totaltax = self_taxpay + spouse_taxpay
				return render_template('joint.html', self_income = self_income, self_mpf = self_mpf, allowance = allowance, self_net_charge_income = self_net_charge_income, self_taxpay = self_taxpay, spouse_income = spouse_income, spouse_mpf = spouse_mpf, spouse_net_charge_income = spouse_net_charge_income, spouse_taxpay = spouse_taxpay, totaltax = totaltax, joint_income = joint_income, joint_mpf = joint_mpf, joint_allowance = joint_allowance, joint_net_charge_income = joint_net_charge_income, joint_taxpay = joint_taxpay)

def single(x):

	income = x
	if income <= 85200:
		mpf = 0
	else:
		mpf = (income*0.05)
		if mpf > 18000:
			mpf = 18000
	allowance = 132000
	net_charge_income = income - mpf - allowance
	net_charge_income_standard = income - mpf 
	if net_charge_income < 0:
		net_charge_income = 0
	if net_charge_income <= 50000:
		tax = int(net_charge_income*0.02)
	elif net_charge_income <= 100000:
		tax = int((net_charge_income-50000)*0.06+1000)
	elif net_charge_income <= 150000:
		tax = int((net_charge_income-100000)*0.1+1000+3000)
	elif net_charge_income <= 200000:
		tax = int((net_charge_income-150000)*0.14+1000+3000+5000)
	elif net_charge_income > 200000:
		tax = int((net_charge_income-200000)*0.17+1000+3000+5000+7000)
	standard_tax = int(net_charge_income_standard*0.15)
	if tax <= standard_tax:
		taxpay = tax
	else:
		taxpay = standard_tax
	return taxpay
			
			
def married(x, y):
	self_income = x
	if self_income <= 85200:
		self_mpf = 0
	else:
		self_mpf = (self_income*0.05)
		if self_mpf > 18000:
			self_mpf = 18000
	allowance = 132000
	self_net_charge_income = self_income - self_mpf - allowance
	self_net_charge_income_standard = self_income - self_mpf
	if self_net_charge_income < 0:
		self_net_charge_income = 0
	if self_net_charge_income <= 50000:
		self_tax = int(self_net_charge_income*0.02)
	elif self_net_charge_income <= 100000:
		self_tax = int((self_net_charge_income-50000)*0.06+1000)
	elif self_net_charge_income <= 150000:
		self_tax = int((self_net_charge_income-100000)*0.1+1000+3000)
	elif self_net_charge_income <= 200000:
		self_tax = int((self_net_charge_income-150000)*0.14+1000+3000+5000)
	elif self_net_charge_income > 200000:
		self_tax = int((self_net_charge_income-200000)*0.17+1000+3000+5000+7000)
	self_standard_tax = int(self_net_charge_income_standard*0.15)
	if self_tax <= self_standard_tax:
		self_taxpay = self_tax
	else:
		self_taxpay = self_standard_tax

	spouse_income = y
	spouse_mpf = int(spouse_income*0.05)
	if spouse_income <= 85200:
		spouse_mpf = 0
	else:
		spouse_mpf = (spouse_income*0.05)
		if spouse_mpf > 18000:
			spouse_mpf = 18000
	spouse_net_charge_income = spouse_income - spouse_mpf - allowance
	spouse_net_charge_income_standard = spouse_income - spouse_mpf 
	if spouse_net_charge_income < 0:
		spouse_net_charge_income = 0
	if spouse_net_charge_income <= 50000:
		spouse_tax = int(spouse_net_charge_income*0.02)
	elif spouse_net_charge_income <= 100000:
		spouse_tax = int((spouse_net_charge_income-50000)*0.06+1000)
	elif spouse_net_charge_income <= 150000:
		spouse_tax = int((spouse_net_charge_income-100000)*0.1+1000+3000)
	elif spouse_net_charge_income <= 200000:
		spouse_tax = int((spouse_net_charge_income-150000)*0.14+1000+3000+5000)
	elif spouse_net_charge_income > 200000:
		spouse_tax = int((spouse_net_charge_income-200000)*0.17+1000+3000+5000+7000)
	spouse_standard_tax = int(spouse_net_charge_income_standard*0.15)
	if spouse_tax <= spouse_standard_tax:
		spouse_taxpay = spouse_tax
	else:
		spouse_taxpay = spouse_standard_tax
	
	joint_income = self_income + spouse_income
	joint_mpf = self_mpf + spouse_mpf

	joint_allowance = allowance*2
	joint_net_charge_income = joint_income - joint_mpf - joint_allowance
	joint_net_charge_income_standard = joint_income - joint_mpf
	if joint_net_charge_income < 0:
		joint_net_charge_income = 0
	if joint_net_charge_income <= 50000:
		joint_tax = int(joint_net_charge_income*0.02)
	elif joint_net_charge_income <= 100000:
		joint_tax = int((joint_net_charge_income-50000)*0.06+1000)
	elif joint_net_charge_income <= 150000:
		joint_tax = int((joint_net_charge_income-100000)*0.1+1000+3000)
	elif joint_net_charge_income <= 200000:
		joint_tax = int((joint_net_charge_income-150000)*0.14+1000+3000+5000)
	elif joint_net_charge_income > 200000:
		joint_tax = int((joint_net_charge_income-200000)*0.17+1000+3000+5000+7000)
	joint_standard_tax = int(joint_net_charge_income_standard*0.15)
	if joint_tax <= joint_standard_tax:
		joint_taxpay = joint_tax
	else:
		joint_taxpay = joint_standard_tax

	if joint_taxpay >= (self_taxpay + spouse_taxpay):
		totaltax = self_taxpay + spouse_taxpay
	else:
		totaltax = joint_taxpay
	return totaltax
	


			
	


if __name__ == '__main__':
	app.run(debug = True,host='0.0.0.0')