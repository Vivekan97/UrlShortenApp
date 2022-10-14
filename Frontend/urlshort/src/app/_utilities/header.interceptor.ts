import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from '../_services/auth.service';

@Injectable()
export class HeaderInterceptor implements HttpInterceptor {

  // accessToken:string | null = null;
  constructor(private auth:AuthService) {
    // this.accessToken = this.auth.getAccessToken();
  }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {

    if(request.headers.has("IgnoreAuth") && request.headers.get("IgnoreAuth")==="true"){
      return next.handle(request)
    }

    let token = localStorage.getItem("accessToken")
    // console.warn("Access", token)
    if(token && !request.headers.has("Authorization") ){

      let authHeader = request.headers.append("Authorization", `Bearer ${JSON.parse(token)}`)
      const securedRequest = request.clone({headers:authHeader})
      return next.handle(securedRequest)
    }
    return next.handle(request);
  }
}
