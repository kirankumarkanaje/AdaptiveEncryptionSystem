import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-encryption-form',
  templateUrl: './encryption-form.component.html',
  styleUrls: ['./encryption-form.component.css']
})
export class EncryptionFormComponent {
  data: string = '';
  sensitivity: number = 5;
  batteryLevel: number = 50;
  result: any = null;

  constructor(private http: HttpClient) {}

  encryptData() {
    const payload = {
      data: this.data,
      sensitivity: this.sensitivity,
      battery_level: this.batteryLevel
    };

    this.http.post('http://127.0.0.1:5000/encrypt', payload).subscribe(
      (response: any) => {
        this.result = response;
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }
}
