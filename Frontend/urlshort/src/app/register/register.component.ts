import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormControl, FormGroup, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  emailRegex:string = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$";
  registerForm!:FormGroup;
  constructor(private fb:FormBuilder) { }

  ngOnInit(): void {
    this.initializeForm();
  }

  initializeForm(){
    this.registerForm = this.fb.group({
      "email":new FormControl(null,[Validators.required, Validators.pattern(this.emailRegex)]),
      "password": new FormControl(null, [Validators.required, Validators.minLength(6)]),
      "confirmPassword": new FormControl(null, [Validators.required, Validators.minLength(6), this.comparePasswords]),
    })
  }

  comparePasswords: ValidatorFn = (group:AbstractControl): ValidationErrors | null =>{
    let pass = group.get('password')?.value;
    let confirmPass = group.get('confirmpassword')?.value;
    // console.log(`${pass} & ${confirmPass}`);
    return pass === confirmPass ? null : {'notSame': true}
  }

  registerUser(){
    console.log("Register Staff !");
  }

}
