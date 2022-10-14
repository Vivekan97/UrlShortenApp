import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormControl, FormGroup, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginResponse } from '../_models/model';
import { AuthService } from '../_services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  emailRegex:string = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$";
  registerForm!:FormGroup;
  errorMessage!:string;
  successMessage:boolean = false;
  constructor(private fb:FormBuilder, private auth:AuthService,
    private router:Router) { }

  ngOnInit(): void {
    if(this.auth.checkStatus()){
      this.router.navigate(["home"])
    }
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
    // console.log(group)
    let pass = this.registerForm?.get('password')?.value;
    let confirmPass = this.registerForm?.get('confirmPassword')?.value;
    // console.log(`${pass} & ${confirmPass}`);
    return pass === confirmPass ? null : {'notSame': true}
  }

  registerUser(){
    // console.log("Register Staff !");
    let username:string = this.registerForm.value["email"];
    let password:string = this.registerForm.value["password"];
    this.auth.registerUser(username, password).subscribe(
      {
        next:(value:LoginResponse)=>{
          this.successMessage = true
        },
        error:(err)=>{
          this.errorMessage = err?.error?.message;
        },
      }
    )
  }

}
