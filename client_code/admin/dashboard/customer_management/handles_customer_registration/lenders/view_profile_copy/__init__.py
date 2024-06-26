from ._anvil_designer import view_profile_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class view_profile_copy(view_profile_copyTemplate):
  def __init__(self, value_to_display, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_user_profile.search()

    self.id_list = []
    self.name_list = []
    self.status_list = []
    self.gender_list = []
    self.age_list = []
    self.dob_list = []
    self.email_user = []
    self.aadhar_list = []
    self.pan_list = []
    self.city_list = []
    self.last_confirm_list = []
    self.mobile_check_list = []
    self.mother_status_list = []
    self.date_marrige_list = []
    self.space_name_list = []
    self.about_list = []
    self.alets_list = []
    self.terms_list = []
    self.qualification_list = []
    self.address = []
    self.address2_type= []
    self.address_type_list = []
    self.Duration_at_address_list = []
    self.profession_type_list = []
    self.street_list = []
    self.build_name_list = []
    self.house_no_list = []
    self.landmark_list = []
    self.pincode_list = []
    self.state_list = []
    self.country = []
    self.spouse_number_list = []
    self.company_name_list = []
    self.company_adress_list = []
    self.proffic_list = []
    self.user_type_list = []
    self.approve_list = []
    self.mobile_list = []
    self.another_email = []
    self.company_name = []
    self.organization_type = []
    self.employment_type = []
    self.business_no = []
    self.company_landmark = []
    self.company_address = []
    self.annual_salary = []
    self.salary_type = []
    self.designation = []
    self.father_name = []
    self.father_age = []
    self.mother_name = []
    self.mother_age = []
    self.college_name = []
    self.college_id = []
    self.college_address = []
    self.running_loan = []
    self.profile = []
    self.aadhaar_photo = []
    self.pan_photo = []
    self.emp_id_proof = []
    self.last_six_month_bank_proof = []
    self.college_proof = []
    self.home_loan = []
    self.other_loan = []
    self.personal_loan = []
    self.vehicle_loan = []

    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['customer_id'])
      self.name_list.append(i['full_name'])
      self.status_list.append(i['profile_status'])
      self.gender_list.append(i['gender'])
      self.age_list.append(i['user_age'])
      self.dob_list.append(i['date_of_birth'])
      self.email_user.append(i['email_user'])
      self.aadhar_list.append(i['aadhaar_no'])
      self.pan_list.append(i['pan_number'])
      self.city_list.append(i['city'])
      self.last_confirm_list.append(i['last_confirm'])
      self.mobile_check_list.append(i['mobile_check'])
      self.mother_status_list.append(i['marital_status'])
      # self.date_marrige_list.append(i['Date_mariage'])
      self.space_name_list.append(i['spouse_name'])
      self.about_list.append(i['about'])
      self.alets_list.append(i['alerts'])
      self.terms_list.append(i['terms'])
      self.qualification_list.append(i['qualification'])
      self.profession_type_list.append(i['profession'])
      self.address.append(i['street_adress_1'])
      self.address2_type.append(i['street_address_2'])
      self.address_type_list.append(i['address_type'])
      self.Duration_at_address_list.append(i['duration_at_address'])
      self.street_list.append(i['street'])
      self.build_name_list.append(i['building_name'])
      self.house_no_list.append(i['house_no'])
      self.landmark_list.append(i['house_landmark'])
      self.pincode_list.append(i['pincode'])
      self.state_list.append(i['state'])
      self.country.append(i['country'])
      self.spouse_number_list.append(i['spouse_mobile'])
      self.company_name_list.append(i['spouse_company_name'])
      self.company_adress_list.append(i['spouse_company_address'])
      self.proffic_list.append(i['spouse_profession'])
      self.user_type_list.append(i['usertype'])
      self.approve_list.append(i['registration_approve'])
      self.mobile_list.append(i['mobile'])
      self.another_email.append(i['another_email'])
      self.company_name.append(i['company_name'])
      self.organization_type.append(i['organization_type'])
      self.employment_type.append(i['employment_type'])
      self.business_no.append(i['business_no'])
      self.company_landmark.append(i['company_landmark'])
      self.company_address.append(i['company_address'])
      self.annual_salary.append(i['annual_salary'])
      self.salary_type.append(i['salary_type'])
      self.designation.append(i['designation'])
      self.father_name.append(i['father_name'])
      self.father_age.append(i['father_age'])
      self.mother_name.append(i['mother_name'])
      self.mother_age.append(i['mother_age'])
      self.college_name.append(i['college_name'])
      self.college_id.append(i['college_id'])
      self.college_address.append(i['college_address'])
      self.profile.append(i['user_photo'])
      self.aadhaar_photo.append(i['aadhaar_photo'])
      self.pan_photo.append(i['pan_photo'])
      self.emp_id_proof.append(i['emp_id_proof'])
      self.last_six_month_bank_proof.append(i['last_six_month_bank_proof'])
      self.college_proof.append(i['college_proof'])
      self.home_loan.append(i['home_loan'])
      self.other_loan.append(i['other_loan'])
      self.personal_loan.append(i['credit_card_loans'])
      self.vehicle_loan.append(i['vehicle_loan'])

    print(self.company_adress_list)
    if a == -1:
      alert("No Data Available Here!!")
    else:
      if value_to_display in self.id_list:
        b = self.id_list.index(value_to_display)
        self.label_3.text = value_to_display

        self.set_label_visibility(self.label_8,self.label_2, self.name_list[b])
        self.set_label_visibility(self.label_9,self.label_4, bool(self.status_list[b]))
        self.set_label_visibility(self.label_39,self.label_5, self.gender_list[b])
        self.set_label_visibility(self.label_40, self.label_6,str(self.age_list[b]) if self.age_list[b] else '')
        self.set_label_visibility(self.label_41,self.label_7, self.dob_list[b])
        self.set_label_visibility(self.label_44,self.label_10, self.mobile_list[b])
        self.set_label_visibility(self.label_45,self.label_11, self.aadhar_list[b])
        self.set_label_visibility(self.label_46,self.label_12, self.pan_list[b])
        self.set_label_visibility(self.label_47,self.label_13, self.city_list[b])
        self.set_label_visibility(self.label_130,self.label_129, self.email_user[b])
        self.set_label_visibility(self.label_49, self.label_15,bool(self.last_confirm_list[b]))
        self.set_label_visibility(self.label_50,self.label_16, self.mobile_check_list[b])
        self.set_label_visibility(self.label_53,self.label_18, self.mother_status_list[b])
        self.set_label_visibility(self.label_54,self.label_20, self.space_name_list[b])
        self.set_label_visibility(self.label_61,self.label_27, self.about_list[b])
        self.set_label_visibility(self.label_63,self.label_29, bool(self.alets_list[b]))
        self.set_label_visibility(self.label_72,self.label_38, bool(self.terms_list[b]))
        self.set_label_visibility(self.label_69,self.label_35, self.qualification_list[b])
        self.set_label_visibility(self.label_136,self.label_135,self.profession_type_list[b])
        self.set_label_visibility(self.label_132,self.label_131, self.address[b])
        self.set_label_visibility(self.label_51,self.label_14, self.address2_type[b])
        self.set_label_visibility(self.label_62,self.label_28, self.address_type_list[b])
        self.set_label_visibility(self.label_138,self.label_67,self.Duration_at_address_list[b])
        self.set_label_visibility(self.label_71,self.label_37, self.street_list[b])
        self.set_label_visibility(self.label_64,self.label_30, self.build_name_list[b])
        self.set_label_visibility(self.label_66,self.label_32, self.house_no_list[b])
        self.set_label_visibility(self.label_65,self.label_31, self.landmark_list[b])
        self.set_label_visibility(self.label_68,self.label_34, self.pincode_list[b])
        self.set_label_visibility(self.label_70,self.label_36, self.state_list[b])
        self.set_label_visibility(self.label_134,self.label_133,self.country[b])
        self.set_label_visibility(self.label_55,self.label_21, self.spouse_number_list[b])
        self.set_label_visibility(self.label_56,self.label_22, self.company_name_list[b])
        self.set_label_visibility(self.label_57, self.label_23,self.company_adress_list[b])
        self.set_label_visibility(self.label_58,self.label_24, self.proffic_list[b])
        self.set_label_visibility(self.label_59,self.label_25, self.user_type_list[b])
        self.set_label_visibility(self.label_60,self.label_26, bool(self.approve_list[b]))
        self.set_label_visibility(self.label_74,self.label_73, self.another_email[b])
        self.set_label_visibility(self.label_57,self.label_24, self.proffic_list[b])
        self.set_label_visibility(self.label_76,self.label_75, self.company_name[b])
        self.set_label_visibility(self.label_77,self.label_42, self.organization_type[b])
        self.set_label_visibility(self.label_79,self.label_78, self.employment_type[b])
        self.set_label_visibility(self.label_81,self.label_80, self.business_no[b])
        self.set_label_visibility(self.label_83,self.label_82, self.company_landmark[b])
        self.set_label_visibility(self.label_85,self.label_84, self.company_address[b])
        self.set_label_visibility(self.label_87,self.label_86, self.annual_salary[b])
        self.set_label_visibility(self.label_98, self.label_97, self.salary_type[b])
        self.set_label_visibility(self.label_89,self.label_88, self.designation[b])
        self.set_label_visibility(self.label_107, self.label_106,self.father_name[b])
        self.set_label_visibility(self.label_109,self.label_108, self.father_age[b])
        self.set_label_visibility(self.label_111,self.label_110, self.mother_name[b])
        self.set_label_visibility(self.label_113,self.label_112, self.mother_age[b])
        self.set_label_visibility(self.label_115,self.label_114, self.college_name[b])
        self.set_label_visibility(self.label_117,self.label_116, self.college_id[b])
        self.set_label_visibility(self.label_119,self.label_118, self.college_address[b])
        self.set_label_visibility(self.label_90,self.label_17, self.home_loan[b])
        self.set_label_visibility(self.label_92,self.label_91, self.other_loan[b])
        self.set_label_visibility(self.label_94,self.label_93, self.personal_loan[b])
        self.set_label_visibility(self.label_96,self.label_95, self.vehicle_loan[b])
        # Set image sources
        self.image_2.source = self.profile[b]
        self.image_3.source = self.aadhaar_photo[b]
        self.image_4.source = self.pan_photo[b]
        self.image_5.source = self.emp_id_proof[b]
        self.image_6.source = self.last_six_month_bank_proof[b]
        self.image_7.source = self.college_proof[b]

  def set_label_visibility(self, label,label_1, data ):
    if data:
        label.text = data
        label.visible = True
        label_1.visible = True
    else:
        label.visible = False
        label_1.visible = False
      
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer_id_value = self.label_3.text
    open_form('admin.dashboard.customer_management.handles_customer_registration.lenders.view_profile_copy.edit_form_copy', customer_id_value)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    customer_id_value = self.label_3.text
    open_form('admin.dashboard.customer_management.handles_customer_registration.lenders.view_profile_copy.update_form_copy', customer_id_value)

  # def button_1_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   open_form('admin.dashboard.lenders')

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.customer_management.handles_customer_registration.lenders')

