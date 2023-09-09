package com.ivanox.godroid;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import utils.Utils;

public class MainActivity extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onSubmit(View v) {
        String licenseKey = ((EditText) findViewById(R.id.editTextLicenseKey)).getText().toString();

        if (Utils.encrypt(licenseKey).equals("6c502456a4b9014a8f75af9319169cf278c59156e6984aad2072a5406cf59eeb7127ec014186ef5a9aa484bbb37277cd411e")) {
            ((TextView)findViewById(R.id.textView)).setText(String.format("Correct! Here's your Flag: COMPFEST15{%s}", licenseKey));
        } else {
            ((TextView)findViewById(R.id.textView)).setText("Wrong!");
        }
    }
}