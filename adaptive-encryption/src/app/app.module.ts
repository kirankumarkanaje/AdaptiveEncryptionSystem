import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { EncryptionFormComponent } from './encryption-form/encryption-form.component';

@NgModule({
  declarations: [
    AppComponent,         // Root component
    EncryptionFormComponent // Form component
  ],
  imports: [
    BrowserModule,        // Required for Angular apps
    FormsModule,           // For ngModel and form handling
    HttpClientModule // Add this
  ],
  providers: [],
  bootstrap: [AppComponent] // Root component to bootstrap
})
export class AppModule { }
