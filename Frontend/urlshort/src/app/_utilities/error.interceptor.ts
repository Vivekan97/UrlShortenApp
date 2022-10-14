import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { AuthService } from '../_services/auth.service';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {

  constructor(private auth:AuthService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if(request.headers.has('IgnoreAuth') && (request.headers.get("IgnoreAuth")==="true")){
      return next.handle(request)
    }
    return next.handle(request).pipe(
      // tap((request:any)=>{
      //   console.log(request)
      // }),
      catchError((error:any)=>{
        // console.log("ERROR -> ",error);
        if(error?.status===401){
          this.auth.logOut();
        }
        return throwError(()=>error)
      })
    );
  }
}
