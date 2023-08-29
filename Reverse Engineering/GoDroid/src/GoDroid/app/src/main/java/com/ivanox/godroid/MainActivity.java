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

        if (Utils.encrypt(licenseKey).equals("650e2014a6d7041d8024a8984e47cc9810cead06b0c24dfc742aa71c6de29cb42679b1544286ed09cbf2d2bebd7c2ccd1148")) {
            ((TextView)findViewById(R.id.textView)).setText(String.format("Correct! Here's your Flag: COMPFEST15{%s}", licenseKey));
        } else {
            ((TextView)findViewById(R.id.textView)).setText("Wrong!");
        }
    }
}