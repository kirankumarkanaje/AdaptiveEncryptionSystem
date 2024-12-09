import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncryptionFormComponent } from './encryption-form.component';

describe('EncryptionFormComponent', () => {
  let component: EncryptionFormComponent;
  let fixture: ComponentFixture<EncryptionFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EncryptionFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EncryptionFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
