<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Hexagonal Architecture: A Pattern for Sustainable Software Development" FOLDED="false" ID="ID_fb20e4e7_3ff6_4371_8110_39105981a4ae" CREATED="1741019243442" MODIFIED="1741019243442"><richcontent TYPE="NOTE">

<html>
                <head/>
                <body>
                    <p>An architectural pattern that allows applications to be driven by various sources and developed independently of runtime environments.</p>
                </body>
            </html>
</richcontent>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false" show_note_icons="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="Core Concepts" POSITION="right" ID="ID_16251746_4826_43b6_93dd_17e9e3e9efb3" CREATED="1741019243442" MODIFIED="1741019243442"><richcontent TYPE="NOTE">

<html>
                    <head/>
                    <body>
                        <p>The foundational ideas that define the structure and operation of Hexagonal Architecture.</p>
                    </body>
                </html>
</richcontent>
<node TEXT="Ports" ID="ID_f3064d32_d590_4c0c_a42d_4653be01af14" CREATED="1741019243442" MODIFIED="1741019243442"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Interfaces that define the boundaries between the application and external systems.</p>
                        </body>
                    </html>
</richcontent>
<node TEXT="Primary Ports" ID="ID_57b97216_8a27_491c_b7c7_af7011f941ee" CREATED="1741019243443" MODIFIED="1741019243443"><richcontent TYPE="NOTE">

<html>
                            <head/>
                            <body>
                                <p>Used by actors to drive the application.</p>
                            </body>
                        </html>
</richcontent>
</node>
<node TEXT="Secondary Ports" ID="ID_24398163_05c6_432b_8fea_c982cc8be1dd" CREATED="1741019243443" MODIFIED="1741019243443"><richcontent TYPE="NOTE">

<html>
                            <head/>
                            <body>
                                <p>Used by the application to communicate with external systems.</p>
                            </body>
                        </html>
</richcontent>
</node>
</node>
<node TEXT="Adapters" ID="ID_ca686686_16c6_4712_b74d_19afc6ba33f6" CREATED="1741019243443" MODIFIED="1741019243443"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Components that implement the interfaces defined by ports, translating between the application and the external world.</p>
                        </body>
                    </html>
</richcontent>
<node TEXT="Primary Adapters" ID="ID_eb335145_e826_4b59_b90a_9f63d266cd52" CREATED="1741019243443" MODIFIED="1741019243443"><richcontent TYPE="NOTE">

<html>
                            <head/>
                            <body>
                                <p>Translate external inputs to application inputs.</p>
                            </body>
                        </html>
</richcontent>
</node>
<node TEXT="Secondary Adapters" ID="ID_868a1f01_acb8_49aa_bda0_36247b8a4b5f" CREATED="1741019243444" MODIFIED="1741019243444"><richcontent TYPE="NOTE">

<html>
                            <head/>
                            <body>
                                <p>Translate application outputs to external outputs.</p>
                            </body>
                        </html>
</richcontent>
</node>
</node>
<node TEXT="Domain" ID="ID_42301c99_f0a3_4a3c_81ad_5e8858dbd725" CREATED="1741019243444" MODIFIED="1741019243444"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Represents the core business logic of the application, isolated from external concerns.</p>
                        </body>
                    </html>
</richcontent>
</node>
</node>
<node TEXT="Benefits" POSITION="left" ID="ID_56689420_38ab_474b_8207_a6fca74a81bb" CREATED="1741019243444" MODIFIED="1741019243444"><richcontent TYPE="NOTE">

<html>
                    <head/>
                    <body>
                        <p>Advantages of using Hexagonal Architecture in software development.</p>
                    </body>
                </html>
</richcontent>
<node TEXT="Testability" ID="ID_f1a596f4_60d2_4764_a6c8_74582094bcfd" CREATED="1741019243444" MODIFIED="1741019243444"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>The domain can be tested in isolation without external dependencies.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Flexibility" ID="ID_145786c8_8bae_433b_bd75_c396779f3a55" CREATED="1741019243445" MODIFIED="1741019243445"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Adapters can be swapped without changing the core logic.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Maintainability" ID="ID_7511c08a_c5c7_4570_92f1_c3a86ccc0fcd" CREATED="1741019243445" MODIFIED="1741019243445"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Clear separation of concerns makes the code easier to maintain.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Technology Independence" ID="ID_db96f530_4683_4580_8422_a75b12022cf1" CREATED="1741019243445" MODIFIED="1741019243445"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>The domain is not tied to specific technologies.</p>
                        </body>
                    </html>
</richcontent>
</node>
</node>
<node TEXT="Implementing Hexagonal Architecture" POSITION="right" ID="ID_0fa0ac0d_0228_4644_8fce_b445c8ea6f83" CREATED="1741019243445" MODIFIED="1741019243445"><richcontent TYPE="NOTE">

<html>
                    <head/>
                    <body>
                        <p>Steps to effectively implement the Hexagonal Architecture pattern.</p>
                    </body>
                </html>
</richcontent>
<node TEXT="Define Domain Model" ID="ID_2b4563a8_321b_420d_a796_0d5b422d65d4" CREATED="1741019243445" MODIFIED="1741019243445"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Start by defining the core business logic of the application.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Create Ports" ID="ID_0c968e4e_22e7_4574_9276_6e5aaae57771" CREATED="1741019243446" MODIFIED="1741019243446"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Develop interfaces for interactions with external systems.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Implement Adapters" ID="ID_d7cc5b11_963f_4cf5_8e2b_4de61690174e" CREATED="1741019243446" MODIFIED="1741019243446"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Build components that fulfill the defined interfaces.</p>
                        </body>
                    </html>
</richcontent>
</node>
<node TEXT="Use Dependency Injection" ID="ID_5999139f_8b69_431c_a3ae_158522311545" CREATED="1741019243446" MODIFIED="1741019243446"><richcontent TYPE="NOTE">

<html>
                        <head/>
                        <body>
                            <p>Connect adapters with the application to maintain focus on domain problems.</p>
                        </body>
                    </html>
</richcontent>
</node>
</node>
</node>
</map>
