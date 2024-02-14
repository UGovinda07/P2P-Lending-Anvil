from ._anvil_designer import wallet_depositTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form, server
# from .. import bmain_form_module as main_form_module
# from ...lendor_registration_form.dashboard import lendor_main_form_module as main_form_module
from ...borrower_registration_form.dashboard import main_form_module
from datetime import datetime, timezone
from datetime import timedelta
import time

class wallet_deposit(wallet_depositTemplate):
  def __init__(self,entered_loan_id,entered_borrower_customer_id, **properties):
    self.entered_loan_id = entered_loan_id
    self.entered_borrower_customer_id = entered_borrower_customer_id
    self.user_id = main_form_module.userId
    self.selected_row = None
    self.start_time = time.time()
    start_time = self.start_time
    
    
    self.check_time_difference()
    

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.deposit_placeholder = "5000"
    self.withdraw_placeholder = "0.00"

    self.email=main_form_module.email
    email = self.email


    wallet_row =app_tables.fin_wallet.get(user_email=email)
    if wallet_row:
      self.balance_lable.text = wallet_row['wallet_amount']

    # self.user_id = main_form_module.userId
    # user_id = self.user_id

    # self.user_id = main_form_module.userId
    # user_id = self.user_id
  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    user_request = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_request:
      self.user_type = user_request['usertype']

    if self.user_type == "lender":
      open_form("lendor_registration_form.dashboard")
    else:
      open_form("borrower_registration_form.dashboard")


  # def about_main_form_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form("lendor_registration_form.dashboard.dasboard_about")

  # def contact_main_form_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form("lendor_registration_form.dashboard.dasboard_contact")

  # def notification_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('lendor_registration_form.dashboard.notification')

  # def button_2_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   pass

  def deposit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.amount_text_box.placeholder = self.deposit_placeholder
    self.deposit_money_btn.visible = True
    self.withdraw_money_btn.visible = False


  def withdraw_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.amount_text_box.placeholder = self.withdraw_placeholder
    self.deposit_money_btn.visible = False
    self.withdraw_money_btn.visible = True
    self.deposit_btn.visible = True

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  
  def deposit_money_btn_click(self, **event_args):
        amount_entered = self.amount_text_box.text

        # Check if amount_entered is not empty and is a valid number
        if not amount_entered or not str(amount_entered).isdigit():
            alert("Please enter a valid amount.")
            return

        try:
            deposit_amount = int(amount_entered)
        except ValueError:
            alert("Please enter a valid amount.")
            return

        customer_id = 1000
        email = self.email
        selected_row = self.selected_row

        if anvil.server.call('deposit_money', email=email, deposit_amount=deposit_amount, customer_id=customer_id):
            alert("Deposit successful!")

            # Update the balance label with the new balance value
            wallet_row = app_tables.fin_wallet.get(user_email=email)
            if wallet_row:
                entered_loan_id = self.entered_loan_id
                loan_row = app_tables.fin_loan_details.get(loan_id=entered_loan_id)
              
                if loan_row:
                    # Get the loan_amount and subtract it from the wallet_amount
                    loan_amount = loan_row['loan_amount']
                    alert(f"Loan amount: {loan_amount}")
                    loan_updated_status = loan_row["loan_updated_status"]
                    loan_disbursed_timestamp = loan_row["loan_disbursed_timestamp"]
                    new_balance = wallet_row['wallet_amount'] - loan_amount

                    self.start_time = time.time()
                    # Update the wallet_amount in fin_wallet
                    wallet_row['wallet_amount'] = new_balance
                    wallet_row.update()

                    # Update the balance label with the new balance value
                    self.balance_lable.text = f"{new_balance}"

                    if loan_disbursed_timestamp is not None:
                        # Update the loan_disbursed_timestamp with the current datetime
                        loan_row['loan_disbursed_timestamp'] = datetime.now()
                    else:
                        # Set the loan_disbursed_timestamp for the first time if it is None
                        loan_row['loan_disbursed_timestamp'] = datetime.now()

                    # Calculate and set the first EMI payment due date (only date portion)
                    emi_payment_type = loan_row['emi_payment_type']
                    loan_disbursed_timestamp = loan_row['loan_disbursed_timestamp']
                    tenure = loan_row['tenure']
                    first_emi_due_date = self.calculate_first_emi_due_date(emi_payment_type, loan_disbursed_timestamp, tenure)

                    loan_row['first_emi_payment_due_date'] = first_emi_due_date

                    entered_borrower_customer_id = self.entered_borrower_customer_id
                    # Convert entered_borrower_customer_id to integer
                    try:
                      entered_borrower_customer_id = int(entered_borrower_customer_id)
                    except ValueError:
                      alert("Please enter a valid customer ID.")
                      return
                    # Search for the row in fin_wallet table
                    wallet_add = app_tables.fin_wallet.get(customer_id=entered_borrower_customer_id)
                    if wallet_add:
                      loan_amount = loan_row['loan_amount']
                      wallet_add['wallet_amount'] += deposit_amount
                      wallet_add.update()

                      # You may want to update the loan_updated_status here if needed
                      updated_loan_status = 'disbursed loan'
                      loan_row['loan_updated_status'] = updated_loan_status
                      # Save the changes to the loan_row
                      loan_row.update()
                      self.check_time_difference()
                  
                      alert(f"Loan Amount Paid to Borrower\nWallet Amount Updated")
                      open_form('lendor_registration_form.dashboard')
                      return
                    else:
                      alert("Wallet not found for the entered borrower customer ID.")     
                else:
                    alert("Loan details not found.")
        else:
            alert("Deposit failed!")

  def check_time_difference(self):
        current_time = datetime.now(timezone.utc)
        # print("current_time:", current_time)
        start_time_utc = datetime.utcfromtimestamp(self.start_time).replace(tzinfo=timezone.utc)
        
        time_difference = current_time - start_time_utc

        if time_difference.total_seconds() > 120:  # 120 seconds = 2 minutes
            # Update loan status based on the comparison of wallet_amount and loan_amount
            
            wallet_row = app_tables.fin_wallet.get(user_email=self.email)
            loan_row = app_tables.fin_loan_details.get(loan_id=self.entered_loan_id)

            if wallet_row and loan_row:
                loan_amount = loan_row['loan_amount']
                wallet_amount = wallet_row['wallet_amount']

                if loan_amount > wallet_amount:
                    # Update loan status to 'lost opportunities'
                    loan_row['loan_updated_status'] = 'lost opportunities'
                    loan_row.update()
                    print("loan_updated_status as lost opportunities")
                    alert("The designated time has passed. The loan has moved to the 'Lost Opportunities' status.")
                    open_form('lendor_registration_form.dashboard')
                else:
                    alert("Time has passed, but wallet_amount is sufficient. No change in loan status.")
                    open_form('lendor_registration_form.dashboard')
            else:
                alert("Error: Wallet or loan details not found.")

   
  def form_show(self, **event_args):
        self.start_time = time.time()  # Set the start time when the form is shown
        self.check_time_difference()

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.check_time_difference()
    # Print time_difference every 30 seconds
    if int(time.time() - self.start_time) % 30 == 0:
      print("time_difference:", datetime.now(timezone.utc) - datetime.utcfromtimestamp(self.start_time).replace(tzinfo=timezone.utc))
  
  def calculate_first_emi_due_date(self, emi_payment_type, loan_disbursed_timestamp, tenure):
        if emi_payment_type == "Monthly":
            first_emi_due_date = (loan_disbursed_timestamp + timedelta(days=30)).date()
        elif emi_payment_type == "Three Month":
            first_emi_due_date = (loan_disbursed_timestamp + timedelta(days=90)).date()
        elif emi_payment_type == "Six Month":
            first_emi_due_date = (loan_disbursed_timestamp + timedelta(days=180)).date()
        elif emi_payment_type == "One Time":
            if tenure:
                # Add the tenure in months to the loan_disbursed_timestamp
                first_emi_due_date = (loan_disbursed_timestamp + timedelta(days=30 * tenure)).date()
            else:
                # Handle the case where tenure is not provided (raise an exception or set to None)
                first_emi_due_date = None
        else:
            # Handle other cases or raise an exception as needed
            first_emi_due_date = None

        return first_emi_due_date

  

  # def timer_1_tick(self, **event_args):
  #       """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
  #       self.start_time = time.time()  # Initialize start_time here
  #       start_time = self.start_time
  #       # Check if 2 minutes have passed
  #       elapsed_time = time.time() - start_time
  #       if elapsed_time >= 120:  # 2 minutes
  #           self.timer_1.enabled = False  # Stop the timer

  #           # Check loan_amount and wallet_amount after 2 minutes
  #           email = self.email
  #           wallet_row = app_tables.fin_wallet.get(user_email=email)
  #           if wallet_row:
  #               new_balance = wallet_row['wallet_amount']

  #               # Retrieve loan details
  #               entered_loan_id = self.entered_loan_id
  #               loan_row = app_tables.fin_loan_details.get(loan_id=entered_loan_id)

  #               if loan_row:
  #                   loan_amount = loan_row['loan_amount']

  #                   if loan_amount > new_balance:
  #                       # Update loan status to 'lost opportunities'
  #                       loan_row['loan_updated_status'] = 'lost opportunities'
  #                       loan_row.update()
  #                       alert("The designated time has passed. The loan has moved to the 'Lost Opportunities' status.")
  #                       open_form('lendor_registration_form.dashboard')
  #                   else:
  #                       alert("The designated time has passed, but the loan_amount is not greater than the wallet_amount.")
  #               else:
  #                   alert("Loan details not found.")
  #           else:
  #               alert("Wallet details not found.")
    
  # def withdraw_money_btn_click(self, **event_args):
  #   amount_entered = self.amount_text_box.text

  #   try:
  #     withdraw_amount = int(amount_entered)
  #   except ValueError:
  #     return

  #   customer_id = 1000
  #   email = self.email

  #   wallet_row = app_tables.fin_wallet.get(user_email=email)

  #   if wallet_row is None:
  #     wallet_row = app_tables.fin_wallet.add_row(user_email=email, wallet_amount=0)

  #   if anvil.server.call('withdraw_money', email=email, withdraw_amount=withdraw_amount, customer_id=customer_id):
  #     alert("Withdrawal successful!")
  #     # Update the balance label with the new balance value
  #     wallet_row = app_tables.fin_wallet.get(user_email=email)
  #     if wallet_row:
  #       self.balance_lable.text = f"{wallet_row['wallet_amount']}"
  #   elif wallet_row is not None and withdraw_amount > wallet_row['wallet_amount']:
  #     alert("Insufficient funds for withdrawal.")
  #   else:
  #     alert("Withdrawal failed!")

  def all_transaction_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("wallet.wallet.all_transaction")

  