PGDMP                         s            skp    9.1.13    9.1.13    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           1262    51445    skp    DATABASE     u   CREATE DATABASE skp WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'es_PY.UTF-8' LC_CTYPE = 'es_PY.UTF-8';
    DROP DATABASE skp;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    5            �           0    0    public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    5            �            3079    11679    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    208            �            1259    51492 
   auth_group    TABLE     �   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    "Fecha" timestamp with time zone,
    "Usuario_id" integer
);
    DROP TABLE public.auth_group;
       public         root    false    5            �            1259    51490    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       root    false    170    5            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       root    false    169            �            1259    51502    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         root    false    5            �            1259    51500    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       root    false    5    172            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       root    false    171            �            1259    51482    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         root    false    5            �            1259    51480    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       root    false    5    168            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       root    false    167            �            1259    51512 	   auth_user    TABLE     ^  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    direccion text,
    observacion text,
    telefono integer,
    CONSTRAINT auth_user_telefono_check CHECK ((telefono >= 0))
);
    DROP TABLE public.auth_user;
       public         root    false    1938    5            �            1259    51522    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         root    false    5            �            1259    51520    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       root    false    5    176            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       root    false    175            �            1259    51510    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       root    false    174    5            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       root    false    173            �            1259    51532    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         root    false    5            �            1259    51530 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       root    false    5    178            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       root    false    177            �            1259    51586    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         root    false    1942    5            �            1259    51584    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       root    false    180    5            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       root    false    179            �            1259    51472    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         root    false    5            �            1259    51470    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       root    false    166    5            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       root    false    165            �            1259    51448    django_migrations    TABLE     �   CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         root    false    5            �            1259    51446    django_migrations_id_seq    SEQUENCE     z   CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       root    false    5    162            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;
            public       root    false    161            �            1259    52140    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         root    false    5            �            1259    51823    flujos_actividad    TABLE     �   CREATE TABLE flujos_actividad (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Orden" integer,
    "idTabla" integer
);
 $   DROP TABLE public.flujos_actividad;
       public         root    false    5            �            1259    51959    flujos_actividad_Doing    TABLE     �   CREATE TABLE "flujos_actividad_Doing" (
    id integer NOT NULL,
    actividad_id integer NOT NULL,
    userstory_id integer NOT NULL
);
 ,   DROP TABLE public."flujos_actividad_Doing";
       public         root    false    5            �            1259    51957    flujos_actividad_Doing_id_seq    SEQUENCE     �   CREATE SEQUENCE "flujos_actividad_Doing_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public."flujos_actividad_Doing_id_seq";
       public       root    false    5    196            �           0    0    flujos_actividad_Doing_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE "flujos_actividad_Doing_id_seq" OWNED BY "flujos_actividad_Doing".id;
            public       root    false    195            �            1259    51969    flujos_actividad_Done    TABLE     �   CREATE TABLE "flujos_actividad_Done" (
    id integer NOT NULL,
    actividad_id integer NOT NULL,
    userstory_id integer NOT NULL
);
 +   DROP TABLE public."flujos_actividad_Done";
       public         root    false    5            �            1259    51967    flujos_actividad_Done_id_seq    SEQUENCE     �   CREATE SEQUENCE "flujos_actividad_Done_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public."flujos_actividad_Done_id_seq";
       public       root    false    5    198            �           0    0    flujos_actividad_Done_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE "flujos_actividad_Done_id_seq" OWNED BY "flujos_actividad_Done".id;
            public       root    false    197            �            1259    51979    flujos_actividad_To_do    TABLE     �   CREATE TABLE "flujos_actividad_To_do" (
    id integer NOT NULL,
    actividad_id integer NOT NULL,
    userstory_id integer NOT NULL
);
 ,   DROP TABLE public."flujos_actividad_To_do";
       public         root    false    5            �            1259    51977    flujos_actividad_To_do_id_seq    SEQUENCE     �   CREATE SEQUENCE "flujos_actividad_To_do_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public."flujos_actividad_To_do_id_seq";
       public       root    false    5    200            �           0    0    flujos_actividad_To_do_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE "flujos_actividad_To_do_id_seq" OWNED BY "flujos_actividad_To_do".id;
            public       root    false    199            �            1259    51821    flujos_actividad_id_seq    SEQUENCE     y   CREATE SEQUENCE flujos_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.flujos_actividad_id_seq;
       public       root    false    5    190            �           0    0    flujos_actividad_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE flujos_actividad_id_seq OWNED BY flujos_actividad.id;
            public       root    false    189            �            1259    51833    flujos_flujo    TABLE       CREATE TABLE flujos_flujo (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Estado" character varying(15) NOT NULL,
    "Descripcion" text,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer,
    "Copia" boolean NOT NULL
);
     DROP TABLE public.flujos_flujo;
       public         root    false    5            �            1259    51846    flujos_flujo_Actividades    TABLE     �   CREATE TABLE "flujos_flujo_Actividades" (
    id integer NOT NULL,
    flujo_id integer NOT NULL,
    actividad_id integer NOT NULL
);
 .   DROP TABLE public."flujos_flujo_Actividades";
       public         root    false    5            �            1259    51844    flujos_flujo_Actividades_id_seq    SEQUENCE     �   CREATE SEQUENCE "flujos_flujo_Actividades_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."flujos_flujo_Actividades_id_seq";
       public       root    false    194    5            �           0    0    flujos_flujo_Actividades_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE "flujos_flujo_Actividades_id_seq" OWNED BY "flujos_flujo_Actividades".id;
            public       root    false    193            �            1259    51831    flujos_flujo_id_seq    SEQUENCE     u   CREATE SEQUENCE flujos_flujo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.flujos_flujo_id_seq;
       public       root    false    5    192            �           0    0    flujos_flujo_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE flujos_flujo_id_seq OWNED BY flujos_flujo.id;
            public       root    false    191            �            1259    51459    mensaje_mensaje    TABLE     �   CREATE TABLE mensaje_mensaje (
    id integer NOT NULL,
    "Usuario_a_enviar_id" integer,
    "Contenido_mensaje" text,
    "Usuario_que_envio_id" integer
);
 #   DROP TABLE public.mensaje_mensaje;
       public         root    false    5            �            1259    51457    mensaje_mensaje_id_seq    SEQUENCE     x   CREATE SEQUENCE mensaje_mensaje_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.mensaje_mensaje_id_seq;
       public       root    false    164    5            �           0    0    mensaje_mensaje_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE mensaje_mensaje_id_seq OWNED BY mensaje_mensaje.id;
            public       root    false    163            �            1259    51736    proyectos_proyecto    TABLE     �  CREATE TABLE proyectos_proyecto (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Fecha_inicio" date,
    "Fecha_finalizacion" date,
    "Cliente" character varying(30),
    "Estado" character varying(15) NOT NULL,
    "Scrum_Master_id" integer,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer,
    "Dia_actual" date NOT NULL,
    "Registro" text,
    "Duracion" integer NOT NULL,
    "Restante" integer NOT NULL,
    sprint_activo boolean NOT NULL,
    CONSTRAINT "proyectos_proyecto_Duracion_check" CHECK (("Duracion" >= 0)),
    CONSTRAINT "proyectos_proyecto_Restante_check" CHECK (("Restante" >= 0))
);
 &   DROP TABLE public.proyectos_proyecto;
       public         root    false    1957    1958    5            �            1259    51749     proyectos_proyecto_Grupo_trabajo    TABLE     �   CREATE TABLE "proyectos_proyecto_Grupo_trabajo" (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);
 6   DROP TABLE public."proyectos_proyecto_Grupo_trabajo";
       public         root    false    5            �            1259    51747 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE     �   CREATE SEQUENCE "proyectos_proyecto_Grupo_trabajo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public."proyectos_proyecto_Grupo_trabajo_id_seq";
       public       root    false    5    188            �           0    0 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE "proyectos_proyecto_Grupo_trabajo_id_seq" OWNED BY "proyectos_proyecto_Grupo_trabajo".id;
            public       root    false    187            �            1259    52047    proyectos_proyecto_Tablas    TABLE     �   CREATE TABLE "proyectos_proyecto_Tablas" (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    flujo_id integer NOT NULL
);
 /   DROP TABLE public."proyectos_proyecto_Tablas";
       public         root    false    5            �            1259    52045     proyectos_proyecto_Tablas_id_seq    SEQUENCE     �   CREATE SEQUENCE "proyectos_proyecto_Tablas_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public."proyectos_proyecto_Tablas_id_seq";
       public       root    false    202    5             	           0    0     proyectos_proyecto_Tablas_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE "proyectos_proyecto_Tablas_id_seq" OWNED BY "proyectos_proyecto_Tablas".id;
            public       root    false    201            �            1259    51734    proyectos_proyecto_id_seq    SEQUENCE     {   CREATE SEQUENCE proyectos_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.proyectos_proyecto_id_seq;
       public       root    false    5    186            	           0    0    proyectos_proyecto_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE proyectos_proyecto_id_seq OWNED BY proyectos_proyecto.id;
            public       root    false    185            �            1259    51694    sprint_sprint    TABLE     .  CREATE TABLE sprint_sprint (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Fecha_inicio" date,
    "Fecha_finalizacion" date,
    "Cliente" character varying(30),
    "Estado" character varying(30) NOT NULL,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer,
    "Proyecto_asignado_id" integer,
    "Duracion" integer NOT NULL,
    is_active boolean NOT NULL,
    "Tabla_asignada_id" integer,
    "Prioridad_mas_alta" integer NOT NULL,
    "Registro" text,
    "Restante" integer NOT NULL,
    CONSTRAINT "sprint_sprint_Duracion_check" CHECK (("Duracion" >= 0)),
    CONSTRAINT "sprint_sprint_Prioridad_mas_alta_check" CHECK (("Prioridad_mas_alta" >= 0)),
    CONSTRAINT "sprint_sprint_Restante_check" CHECK (("Restante" >= 0))
);
 !   DROP TABLE public.sprint_sprint;
       public         root    false    1953    1954    1955    5            �            1259    52152    sprint_sprint_UserStorys    TABLE     �   CREATE TABLE "sprint_sprint_UserStorys" (
    id integer NOT NULL,
    sprint_id integer NOT NULL,
    userstory_id integer NOT NULL
);
 .   DROP TABLE public."sprint_sprint_UserStorys";
       public         root    false    5            �            1259    52150    sprint_sprint_UserStorys_id_seq    SEQUENCE     �   CREATE SEQUENCE "sprint_sprint_UserStorys_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."sprint_sprint_UserStorys_id_seq";
       public       root    false    205    5            	           0    0    sprint_sprint_UserStorys_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE "sprint_sprint_UserStorys_id_seq" OWNED BY "sprint_sprint_UserStorys".id;
            public       root    false    204            �            1259    51692    sprint_sprint_id_seq    SEQUENCE     v   CREATE SEQUENCE sprint_sprint_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.sprint_sprint_id_seq;
       public       root    false    184    5            	           0    0    sprint_sprint_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE sprint_sprint_id_seq OWNED BY sprint_sprint.id;
            public       root    false    183            �            1259    52338    userstory_cargarhoras    TABLE     �   CREATE TABLE userstory_cargarhoras (
    id integer NOT NULL,
    "Horas" integer,
    "Descripcion" text,
    "US_asignado_id" integer,
    CONSTRAINT "userstory_cargarhoras_Horas_check" CHECK (("Horas" >= 0))
);
 )   DROP TABLE public.userstory_cargarhoras;
       public         root    false    1969    5            �            1259    52336    userstory_cargarhoras_id_seq    SEQUENCE     ~   CREATE SEQUENCE userstory_cargarhoras_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.userstory_cargarhoras_id_seq;
       public       root    false    207    5            	           0    0    userstory_cargarhoras_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE userstory_cargarhoras_id_seq OWNED BY userstory_cargarhoras.id;
            public       root    false    206            �            1259    51665    userstory_userstory    TABLE     �  CREATE TABLE userstory_userstory (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Valor_tecnico" integer,
    "Valor_de_negocio" integer,
    "Size" integer,
    "Estado" character varying(30) NOT NULL,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_asignado_id" integer,
    "Usuario_creador_id" integer,
    "Proyecto_asignado_id" integer,
    is_active boolean NOT NULL,
    in_kanban boolean NOT NULL,
    "Estado_de_actividad" character varying(30) NOT NULL,
    "Actividad_asignada_id" integer,
    "Sub_version" integer,
    "Version" integer,
    "Duracion" integer NOT NULL,
    "Prioridad" integer NOT NULL,
    "Bloqueado" boolean NOT NULL,
    "Registro" text,
    "Restante" integer NOT NULL,
    "Fecha_finalizacion" date,
    "Fecha_inicio" date,
    CONSTRAINT "userstory_userstory_Duracion_check" CHECK (("Duracion" >= 0)),
    CONSTRAINT "userstory_userstory_Prioridad_check" CHECK (("Prioridad" >= 0)),
    CONSTRAINT "userstory_userstory_Restante_check" CHECK (("Restante" >= 0)),
    CONSTRAINT "userstory_userstory_Size_check" CHECK (("Size" >= 0)),
    CONSTRAINT "userstory_userstory_Sub_version_check" CHECK (("Sub_version" >= 0)),
    CONSTRAINT "userstory_userstory_Valor_de_negocio_check" CHECK (("Valor_de_negocio" >= 0)),
    CONSTRAINT "userstory_userstory_Valor_tecnico_check" CHECK (("Valor_tecnico" >= 0)),
    CONSTRAINT "userstory_userstory_Version_check" CHECK (("Version" >= 0))
);
 '   DROP TABLE public.userstory_userstory;
       public         root    false    1944    1945    1946    1947    1948    1949    1950    1951    5            �            1259    51663    userstory_userstory_id_seq    SEQUENCE     |   CREATE SEQUENCE userstory_userstory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.userstory_userstory_id_seq;
       public       root    false    182    5            	           0    0    userstory_userstory_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE userstory_userstory_id_seq OWNED BY userstory_userstory.id;
            public       root    false    181            �           2604    51495    id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       root    false    169    170    170            �           2604    51505    id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    171    172    172            �           2604    51485    id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       root    false    168    167    168            �           2604    51515    id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       root    false    173    174    174            �           2604    51525    id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       root    false    176    175    176            �           2604    51535    id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    178    177    178            �           2604    51589    id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       root    false    179    180    180            �           2604    51475    id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       root    false    165    166    166            �           2604    51451    id    DEFAULT     n   ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       root    false    161    162    162            �           2604    51826    id    DEFAULT     l   ALTER TABLE ONLY flujos_actividad ALTER COLUMN id SET DEFAULT nextval('flujos_actividad_id_seq'::regclass);
 B   ALTER TABLE public.flujos_actividad ALTER COLUMN id DROP DEFAULT;
       public       root    false    189    190    190            �           2604    51962    id    DEFAULT     |   ALTER TABLE ONLY "flujos_actividad_Doing" ALTER COLUMN id SET DEFAULT nextval('"flujos_actividad_Doing_id_seq"'::regclass);
 J   ALTER TABLE public."flujos_actividad_Doing" ALTER COLUMN id DROP DEFAULT;
       public       root    false    196    195    196            �           2604    51972    id    DEFAULT     z   ALTER TABLE ONLY "flujos_actividad_Done" ALTER COLUMN id SET DEFAULT nextval('"flujos_actividad_Done_id_seq"'::regclass);
 I   ALTER TABLE public."flujos_actividad_Done" ALTER COLUMN id DROP DEFAULT;
       public       root    false    198    197    198            �           2604    51982    id    DEFAULT     |   ALTER TABLE ONLY "flujos_actividad_To_do" ALTER COLUMN id SET DEFAULT nextval('"flujos_actividad_To_do_id_seq"'::regclass);
 J   ALTER TABLE public."flujos_actividad_To_do" ALTER COLUMN id DROP DEFAULT;
       public       root    false    200    199    200            �           2604    51836    id    DEFAULT     d   ALTER TABLE ONLY flujos_flujo ALTER COLUMN id SET DEFAULT nextval('flujos_flujo_id_seq'::regclass);
 >   ALTER TABLE public.flujos_flujo ALTER COLUMN id DROP DEFAULT;
       public       root    false    192    191    192            �           2604    51849    id    DEFAULT     �   ALTER TABLE ONLY "flujos_flujo_Actividades" ALTER COLUMN id SET DEFAULT nextval('"flujos_flujo_Actividades_id_seq"'::regclass);
 L   ALTER TABLE public."flujos_flujo_Actividades" ALTER COLUMN id DROP DEFAULT;
       public       root    false    194    193    194            �           2604    51462    id    DEFAULT     j   ALTER TABLE ONLY mensaje_mensaje ALTER COLUMN id SET DEFAULT nextval('mensaje_mensaje_id_seq'::regclass);
 A   ALTER TABLE public.mensaje_mensaje ALTER COLUMN id DROP DEFAULT;
       public       root    false    163    164    164            �           2604    51739    id    DEFAULT     p   ALTER TABLE ONLY proyectos_proyecto ALTER COLUMN id SET DEFAULT nextval('proyectos_proyecto_id_seq'::regclass);
 D   ALTER TABLE public.proyectos_proyecto ALTER COLUMN id DROP DEFAULT;
       public       root    false    186    185    186            �           2604    51752    id    DEFAULT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo" ALTER COLUMN id SET DEFAULT nextval('"proyectos_proyecto_Grupo_trabajo_id_seq"'::regclass);
 T   ALTER TABLE public."proyectos_proyecto_Grupo_trabajo" ALTER COLUMN id DROP DEFAULT;
       public       root    false    187    188    188            �           2604    52050    id    DEFAULT     �   ALTER TABLE ONLY "proyectos_proyecto_Tablas" ALTER COLUMN id SET DEFAULT nextval('"proyectos_proyecto_Tablas_id_seq"'::regclass);
 M   ALTER TABLE public."proyectos_proyecto_Tablas" ALTER COLUMN id DROP DEFAULT;
       public       root    false    202    201    202            �           2604    51697    id    DEFAULT     f   ALTER TABLE ONLY sprint_sprint ALTER COLUMN id SET DEFAULT nextval('sprint_sprint_id_seq'::regclass);
 ?   ALTER TABLE public.sprint_sprint ALTER COLUMN id DROP DEFAULT;
       public       root    false    183    184    184            �           2604    52155    id    DEFAULT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys" ALTER COLUMN id SET DEFAULT nextval('"sprint_sprint_UserStorys_id_seq"'::regclass);
 L   ALTER TABLE public."sprint_sprint_UserStorys" ALTER COLUMN id DROP DEFAULT;
       public       root    false    204    205    205            �           2604    52341    id    DEFAULT     v   ALTER TABLE ONLY userstory_cargarhoras ALTER COLUMN id SET DEFAULT nextval('userstory_cargarhoras_id_seq'::regclass);
 G   ALTER TABLE public.userstory_cargarhoras ALTER COLUMN id DROP DEFAULT;
       public       root    false    206    207    207            �           2604    51668    id    DEFAULT     r   ALTER TABLE ONLY userstory_userstory ALTER COLUMN id SET DEFAULT nextval('userstory_userstory_id_seq'::regclass);
 E   ALTER TABLE public.userstory_userstory ALTER COLUMN id DROP DEFAULT;
       public       root    false    182    181    182            �          0    51492 
   auth_group 
   TABLE DATA               >   COPY auth_group (id, name, "Fecha", "Usuario_id") FROM stdin;
    public       root    false    170    2279   o      	           0    0    auth_group_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('auth_group_id_seq', 1, true);
            public       root    false    169            �          0    51502    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       root    false    172    2279   Wo      	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 47, true);
            public       root    false    171            �          0    51482    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       root    false    168    2279   p      	           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 47, true);
            public       root    false    167            �          0    51512 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, direccion, observacion, telefono) FROM stdin;
    public       root    false    174    2279   Jr      �          0    51522    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       root    false    176    2279   vs      		           0    0    auth_user_groups_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, true);
            public       root    false    175            
	           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 2, true);
            public       root    false    173            �          0    51532    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       root    false    178    2279   �s      	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       root    false    177            �          0    51586    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       root    false    180    2279   �s      	           0    0    django_admin_log_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('django_admin_log_id_seq', 2, true);
            public       root    false    179            �          0    51472    django_content_type 
   TABLE DATA               B   COPY django_content_type (id, name, app_label, model) FROM stdin;
    public       root    false    166    2279   +t      	           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 13, true);
            public       root    false    165            �          0    51448    django_migrations 
   TABLE DATA               <   COPY django_migrations (id, app, name, applied) FROM stdin;
    public       root    false    162    2279   �t      	           0    0    django_migrations_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('django_migrations_id_seq', 106, true);
            public       root    false    161            �          0    52140    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       root    false    203    2279   �{      �          0    51823    flujos_actividad 
   TABLE DATA               E   COPY flujos_actividad (id, "Nombre", "Orden", "idTabla") FROM stdin;
    public       root    false    190    2279   }      �          0    51959    flujos_actividad_Doing 
   TABLE DATA               K   COPY "flujos_actividad_Doing" (id, actividad_id, userstory_id) FROM stdin;
    public       root    false    196    2279   �}      	           0    0    flujos_actividad_Doing_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('"flujos_actividad_Doing_id_seq"', 1, false);
            public       root    false    195            �          0    51969    flujos_actividad_Done 
   TABLE DATA               J   COPY "flujos_actividad_Done" (id, actividad_id, userstory_id) FROM stdin;
    public       root    false    198    2279   �}      	           0    0    flujos_actividad_Done_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('"flujos_actividad_Done_id_seq"', 1, false);
            public       root    false    197            �          0    51979    flujos_actividad_To_do 
   TABLE DATA               K   COPY "flujos_actividad_To_do" (id, actividad_id, userstory_id) FROM stdin;
    public       root    false    200    2279   �}      	           0    0    flujos_actividad_To_do_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('"flujos_actividad_To_do_id_seq"', 1, false);
            public       root    false    199            	           0    0    flujos_actividad_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('flujos_actividad_id_seq', 1, false);
            public       root    false    189            �          0    51833    flujos_flujo 
   TABLE DATA               w   COPY flujos_flujo (id, "Nombre", "Estado", "Descripcion", "Fecha_creacion", "Usuario_creador_id", "Copia") FROM stdin;
    public       root    false    192    2279   �}      �          0    51846    flujos_flujo_Actividades 
   TABLE DATA               I   COPY "flujos_flujo_Actividades" (id, flujo_id, actividad_id) FROM stdin;
    public       root    false    194    2279   ~      	           0    0    flujos_flujo_Actividades_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('"flujos_flujo_Actividades_id_seq"', 1, false);
            public       root    false    193            	           0    0    flujos_flujo_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('flujos_flujo_id_seq', 1, false);
            public       root    false    191            �          0    51459    mensaje_mensaje 
   TABLE DATA               j   COPY mensaje_mensaje (id, "Usuario_a_enviar_id", "Contenido_mensaje", "Usuario_que_envio_id") FROM stdin;
    public       root    false    164    2279   -~      	           0    0    mensaje_mensaje_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('mensaje_mensaje_id_seq', 1, false);
            public       root    false    163            �          0    51736    proyectos_proyecto 
   TABLE DATA               �   COPY proyectos_proyecto (id, "Nombre", "Descripcion", "Fecha_inicio", "Fecha_finalizacion", "Cliente", "Estado", "Scrum_Master_id", "Fecha_creacion", "Usuario_creador_id", "Dia_actual", "Registro", "Duracion", "Restante", sprint_activo) FROM stdin;
    public       root    false    186    2279   J~      �          0    51749     proyectos_proyecto_Grupo_trabajo 
   TABLE DATA               O   COPY "proyectos_proyecto_Grupo_trabajo" (id, proyecto_id, user_id) FROM stdin;
    public       root    false    188    2279   g~      	           0    0 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('"proyectos_proyecto_Grupo_trabajo_id_seq"', 1, false);
            public       root    false    187            �          0    52047    proyectos_proyecto_Tablas 
   TABLE DATA               I   COPY "proyectos_proyecto_Tablas" (id, proyecto_id, flujo_id) FROM stdin;
    public       root    false    202    2279   �~      	           0    0     proyectos_proyecto_Tablas_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('"proyectos_proyecto_Tablas_id_seq"', 1, false);
            public       root    false    201            	           0    0    proyectos_proyecto_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('proyectos_proyecto_id_seq', 1, false);
            public       root    false    185            �          0    51694    sprint_sprint 
   TABLE DATA                 COPY sprint_sprint (id, "Nombre", "Descripcion", "Fecha_inicio", "Fecha_finalizacion", "Cliente", "Estado", "Fecha_creacion", "Usuario_creador_id", "Proyecto_asignado_id", "Duracion", is_active, "Tabla_asignada_id", "Prioridad_mas_alta", "Registro", "Restante") FROM stdin;
    public       root    false    184    2279   �~      �          0    52152    sprint_sprint_UserStorys 
   TABLE DATA               J   COPY "sprint_sprint_UserStorys" (id, sprint_id, userstory_id) FROM stdin;
    public       root    false    205    2279   �~      	           0    0    sprint_sprint_UserStorys_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('"sprint_sprint_UserStorys_id_seq"', 1, false);
            public       root    false    204            	           0    0    sprint_sprint_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('sprint_sprint_id_seq', 1, false);
            public       root    false    183            �          0    52338    userstory_cargarhoras 
   TABLE DATA               V   COPY userstory_cargarhoras (id, "Horas", "Descripcion", "US_asignado_id") FROM stdin;
    public       root    false    207    2279   �~      	           0    0    userstory_cargarhoras_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('userstory_cargarhoras_id_seq', 1, false);
            public       root    false    206            �          0    51665    userstory_userstory 
   TABLE DATA               �  COPY userstory_userstory (id, "Nombre", "Descripcion", "Valor_tecnico", "Valor_de_negocio", "Size", "Estado", "Fecha_creacion", "Usuario_asignado_id", "Usuario_creador_id", "Proyecto_asignado_id", is_active, in_kanban, "Estado_de_actividad", "Actividad_asignada_id", "Sub_version", "Version", "Duracion", "Prioridad", "Bloqueado", "Registro", "Restante", "Fecha_finalizacion", "Fecha_inicio") FROM stdin;
    public       root    false    182    2279   �~      	           0    0    userstory_userstory_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('userstory_userstory_id_seq', 1, false);
            public       root    false    181            �           2606    51499    auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         root    false    170    170    2280            �           2606    51509 1   auth_group_permissions_group_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);
 r   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
       public         root    false    172    172    172    2280            �           2606    51507    auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         root    false    172    172    2280            �           2606    51497    auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         root    false    170    170    2280            �           2606    51489 ,   auth_permission_content_type_id_codename_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);
 f   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
       public         root    false    168    168    168    2280            �           2606    51487    auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         root    false    168    168    2280            �           2606    51527    auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         root    false    176    176    2280            �           2606    51529 %   auth_user_groups_user_id_group_id_key 
   CONSTRAINT     w   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);
 `   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
       public         root    false    176    176    176    2280            �           2606    51517    auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         root    false    174    174    2280            �           2606    51537    auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         root    false    178    178    2280            �           2606    51539 4   auth_user_user_permissions_user_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);
 y   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
       public         root    false    178    178    178    2280            �           2606    51519    auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         root    false    174    174    2280            �           2606    51595    django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         root    false    180    180    2280            �           2606    51479 3   django_content_type_app_label_45f3b1d93ec8c61c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);
 q   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq;
       public         root    false    166    166    166    2280            �           2606    51477    django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         root    false    166    166    2280            �           2606    51456    django_migrations_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         root    false    162    162    2280            %           2606    52147    django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         root    false    203    203    2280                       2606    51966 4   flujos_actividad_Doing_actividad_id_userstory_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Doing"
    ADD CONSTRAINT "flujos_actividad_Doing_actividad_id_userstory_id_key" UNIQUE (actividad_id, userstory_id);
 y   ALTER TABLE ONLY public."flujos_actividad_Doing" DROP CONSTRAINT "flujos_actividad_Doing_actividad_id_userstory_id_key";
       public         root    false    196    196    196    2280                       2606    51964    flujos_actividad_Doing_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY "flujos_actividad_Doing"
    ADD CONSTRAINT "flujos_actividad_Doing_pkey" PRIMARY KEY (id);
 `   ALTER TABLE ONLY public."flujos_actividad_Doing" DROP CONSTRAINT "flujos_actividad_Doing_pkey";
       public         root    false    196    196    2280                       2606    51976 3   flujos_actividad_Done_actividad_id_userstory_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Done"
    ADD CONSTRAINT "flujos_actividad_Done_actividad_id_userstory_id_key" UNIQUE (actividad_id, userstory_id);
 w   ALTER TABLE ONLY public."flujos_actividad_Done" DROP CONSTRAINT "flujos_actividad_Done_actividad_id_userstory_id_key";
       public         root    false    198    198    198    2280                       2606    51974    flujos_actividad_Done_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY "flujos_actividad_Done"
    ADD CONSTRAINT "flujos_actividad_Done_pkey" PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public."flujos_actividad_Done" DROP CONSTRAINT "flujos_actividad_Done_pkey";
       public         root    false    198    198    2280                       2606    51986 4   flujos_actividad_To_do_actividad_id_userstory_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_To_do"
    ADD CONSTRAINT "flujos_actividad_To_do_actividad_id_userstory_id_key" UNIQUE (actividad_id, userstory_id);
 y   ALTER TABLE ONLY public."flujos_actividad_To_do" DROP CONSTRAINT "flujos_actividad_To_do_actividad_id_userstory_id_key";
       public         root    false    200    200    200    2280                       2606    51984    flujos_actividad_To_do_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY "flujos_actividad_To_do"
    ADD CONSTRAINT "flujos_actividad_To_do_pkey" PRIMARY KEY (id);
 `   ALTER TABLE ONLY public."flujos_actividad_To_do" DROP CONSTRAINT "flujos_actividad_To_do_pkey";
       public         root    false    200    200    2280                        2606    51828    flujos_actividad_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY flujos_actividad
    ADD CONSTRAINT flujos_actividad_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.flujos_actividad DROP CONSTRAINT flujos_actividad_pkey;
       public         root    false    190    190    2280                       2606    51853 2   flujos_flujo_Actividades_flujo_id_actividad_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Actividades_flujo_id_actividad_id_key" UNIQUE (flujo_id, actividad_id);
 y   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Actividades_flujo_id_actividad_id_key";
       public         root    false    194    194    194    2280            
           2606    51851    flujos_flujo_Actividades_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Actividades_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Actividades_pkey";
       public         root    false    194    194    2280                       2606    51841    flujos_flujo_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY flujos_flujo
    ADD CONSTRAINT flujos_flujo_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.flujos_flujo DROP CONSTRAINT flujos_flujo_pkey;
       public         root    false    192    192    2280            �           2606    51467    mensaje_mensaje_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY mensaje_mensaje
    ADD CONSTRAINT mensaje_mensaje_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.mensaje_mensaje DROP CONSTRAINT mensaje_mensaje_pkey;
       public         root    false    164    164    2280            �           2606    51754 %   proyectos_proyecto_Grupo_trabajo_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Grupo_trabajo_pkey" PRIMARY KEY (id);
 t   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Grupo_trabajo_pkey";
       public         root    false    188    188    2280            �           2606    51756 8   proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key" UNIQUE (proyecto_id, user_id);
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key";
       public         root    false    188    188    188    2280            �           2606    51746    proyectos_proyecto_Nombre_key 
   CONSTRAINT     j   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_proyecto_Nombre_key" UNIQUE ("Nombre");
 \   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_proyecto_Nombre_key";
       public         root    false    186    186    2280                        2606    52052    proyectos_proyecto_Tablas_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY "proyectos_proyecto_Tablas"
    ADD CONSTRAINT "proyectos_proyecto_Tablas_pkey" PRIMARY KEY (id);
 f   ALTER TABLE ONLY public."proyectos_proyecto_Tablas" DROP CONSTRAINT "proyectos_proyecto_Tablas_pkey";
       public         root    false    202    202    2280            "           2606    52054 2   proyectos_proyecto_Tablas_proyecto_id_flujo_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Tablas"
    ADD CONSTRAINT "proyectos_proyecto_Tablas_proyecto_id_flujo_id_key" UNIQUE (proyecto_id, flujo_id);
 z   ALTER TABLE ONLY public."proyectos_proyecto_Tablas" DROP CONSTRAINT "proyectos_proyecto_Tablas_proyecto_id_flujo_id_key";
       public         root    false    202    202    202    2280            �           2606    51744    proyectos_proyecto_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT proyectos_proyecto_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT proyectos_proyecto_pkey;
       public         root    false    186    186    2280            �           2606    51704    sprint_sprint_Nombre_key 
   CONSTRAINT     `   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "sprint_sprint_Nombre_key" UNIQUE ("Nombre");
 R   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "sprint_sprint_Nombre_key";
       public         root    false    184    184    2280            *           2606    52157    sprint_sprint_UserStorys_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_UserStorys_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_UserStorys_pkey";
       public         root    false    205    205    2280            ,           2606    52159 3   sprint_sprint_UserStorys_sprint_id_userstory_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_UserStorys_sprint_id_userstory_id_key" UNIQUE (sprint_id, userstory_id);
 z   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_UserStorys_sprint_id_userstory_id_key";
       public         root    false    205    205    205    2280            �           2606    51702    sprint_sprint_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT sprint_sprint_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT sprint_sprint_pkey;
       public         root    false    184    184    2280            /           2606    52347    userstory_cargarhoras_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY userstory_cargarhoras
    ADD CONSTRAINT userstory_cargarhoras_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.userstory_cargarhoras DROP CONSTRAINT userstory_cargarhoras_pkey;
       public         root    false    207    207    2280            �           2606    51676    userstory_userstory_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT userstory_userstory_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT userstory_userstory_pkey;
       public         root    false    182    182    2280            �           1259    51657    auth_group_ae6be32e    INDEX     K   CREATE INDEX auth_group_ae6be32e ON auth_group USING btree ("Usuario_id");
 '   DROP INDEX public.auth_group_ae6be32e;
       public         root    false    170    2280            �           1259    51546 %   auth_group_name_253ae2a6331666e8_like    INDEX     i   CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);
 9   DROP INDEX public.auth_group_name_253ae2a6331666e8_like;
       public         root    false    170    2280            �           1259    51557    auth_group_permissions_0e939a4f    INDEX     _   CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);
 3   DROP INDEX public.auth_group_permissions_0e939a4f;
       public         root    false    172    2280            �           1259    51558    auth_group_permissions_8373b171    INDEX     d   CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);
 3   DROP INDEX public.auth_group_permissions_8373b171;
       public         root    false    172    2280            �           1259    51545    auth_permission_417f1b1c    INDEX     X   CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);
 ,   DROP INDEX public.auth_permission_417f1b1c;
       public         root    false    168    2280            �           1259    51571    auth_user_groups_0e939a4f    INDEX     S   CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);
 -   DROP INDEX public.auth_user_groups_0e939a4f;
       public         root    false    176    2280            �           1259    51570    auth_user_groups_e8701ad4    INDEX     R   CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);
 -   DROP INDEX public.auth_user_groups_e8701ad4;
       public         root    false    176    2280            �           1259    51583 #   auth_user_user_permissions_8373b171    INDEX     l   CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);
 7   DROP INDEX public.auth_user_user_permissions_8373b171;
       public         root    false    178    2280            �           1259    51582 #   auth_user_user_permissions_e8701ad4    INDEX     f   CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);
 7   DROP INDEX public.auth_user_user_permissions_e8701ad4;
       public         root    false    178    2280            �           1259    51559 (   auth_user_username_51b3b110094b8aae_like    INDEX     o   CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);
 <   DROP INDEX public.auth_user_username_51b3b110094b8aae_like;
       public         root    false    174    2280            �           1259    51606    django_admin_log_417f1b1c    INDEX     Z   CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);
 -   DROP INDEX public.django_admin_log_417f1b1c;
       public         root    false    180    2280            �           1259    51607    django_admin_log_e8701ad4    INDEX     R   CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);
 -   DROP INDEX public.django_admin_log_e8701ad4;
       public         root    false    180    2280            #           1259    52148    django_session_de54fa62    INDEX     R   CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);
 +   DROP INDEX public.django_session_de54fa62;
       public         root    false    203    2280            &           1259    52149 0   django_session_session_key_461cfeaa630ca218_like    INDEX        CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);
 D   DROP INDEX public.django_session_session_key_461cfeaa630ca218_like;
       public         root    false    203    2280                       1259    51998    flujos_actividad_Doing_4d4c3b6a    INDEX     g   CREATE INDEX "flujos_actividad_Doing_4d4c3b6a" ON "flujos_actividad_Doing" USING btree (userstory_id);
 5   DROP INDEX public."flujos_actividad_Doing_4d4c3b6a";
       public         root    false    196    2280                       1259    51997    flujos_actividad_Doing_6f919ae9    INDEX     g   CREATE INDEX "flujos_actividad_Doing_6f919ae9" ON "flujos_actividad_Doing" USING btree (actividad_id);
 5   DROP INDEX public."flujos_actividad_Doing_6f919ae9";
       public         root    false    196    2280                       1259    52010    flujos_actividad_Done_4d4c3b6a    INDEX     e   CREATE INDEX "flujos_actividad_Done_4d4c3b6a" ON "flujos_actividad_Done" USING btree (userstory_id);
 4   DROP INDEX public."flujos_actividad_Done_4d4c3b6a";
       public         root    false    198    2280                       1259    52009    flujos_actividad_Done_6f919ae9    INDEX     e   CREATE INDEX "flujos_actividad_Done_6f919ae9" ON "flujos_actividad_Done" USING btree (actividad_id);
 4   DROP INDEX public."flujos_actividad_Done_6f919ae9";
       public         root    false    198    2280            �           1259    51854 -   flujos_actividad_Nombre_42c266ccd5b5837d_like    INDEX     }   CREATE INDEX "flujos_actividad_Nombre_42c266ccd5b5837d_like" ON flujos_actividad USING btree ("Nombre" varchar_pattern_ops);
 C   DROP INDEX public."flujos_actividad_Nombre_42c266ccd5b5837d_like";
       public         root    false    190    2280                       1259    52022    flujos_actividad_To_do_4d4c3b6a    INDEX     g   CREATE INDEX "flujos_actividad_To_do_4d4c3b6a" ON "flujos_actividad_To_do" USING btree (userstory_id);
 5   DROP INDEX public."flujos_actividad_To_do_4d4c3b6a";
       public         root    false    200    2280                       1259    52021    flujos_actividad_To_do_6f919ae9    INDEX     g   CREATE INDEX "flujos_actividad_To_do_6f919ae9" ON "flujos_actividad_To_do" USING btree (actividad_id);
 5   DROP INDEX public."flujos_actividad_To_do_6f919ae9";
       public         root    false    200    2280                       1259    51860    flujos_flujo_56ac0855    INDEX     W   CREATE INDEX flujos_flujo_56ac0855 ON flujos_flujo USING btree ("Usuario_creador_id");
 )   DROP INDEX public.flujos_flujo_56ac0855;
       public         root    false    192    2280                       1259    51873 !   flujos_flujo_Actividades_6f919ae9    INDEX     k   CREATE INDEX "flujos_flujo_Actividades_6f919ae9" ON "flujos_flujo_Actividades" USING btree (actividad_id);
 7   DROP INDEX public."flujos_flujo_Actividades_6f919ae9";
       public         root    false    194    2280                       1259    51872 !   flujos_flujo_Actividades_bd1d5624    INDEX     g   CREATE INDEX "flujos_flujo_Actividades_bd1d5624" ON "flujos_flujo_Actividades" USING btree (flujo_id);
 7   DROP INDEX public."flujos_flujo_Actividades_bd1d5624";
       public         root    false    194    2280                       1259    51861 (   flujos_flujo_Nombre_80ac4eefc469076_like    INDEX     t   CREATE INDEX "flujos_flujo_Nombre_80ac4eefc469076_like" ON flujos_flujo USING btree ("Nombre" varchar_pattern_ops);
 >   DROP INDEX public."flujos_flujo_Nombre_80ac4eefc469076_like";
       public         root    false    192    2280            �           1259    51468 #   mensaje_mensaje_Usuario_a_enviar_id    INDEX     k   CREATE INDEX "mensaje_mensaje_Usuario_a_enviar_id" ON mensaje_mensaje USING btree ("Usuario_a_enviar_id");
 9   DROP INDEX public."mensaje_mensaje_Usuario_a_enviar_id";
       public         root    false    164    2280            �           1259    51469 $   mensaje_mensaje_Usuario_que_envio_id    INDEX     m   CREATE INDEX "mensaje_mensaje_Usuario_que_envio_id" ON mensaje_mensaje USING btree ("Usuario_que_envio_id");
 :   DROP INDEX public."mensaje_mensaje_Usuario_que_envio_id";
       public         root    false    164    2280            �           1259    51776    proyectos_proyecto_56ac0855    INDEX     c   CREATE INDEX proyectos_proyecto_56ac0855 ON proyectos_proyecto USING btree ("Usuario_creador_id");
 /   DROP INDEX public.proyectos_proyecto_56ac0855;
       public         root    false    186    2280            �           1259    51775 )   proyectos_proyecto_Grupo_trabajo_e8701ad4    INDEX     v   CREATE INDEX "proyectos_proyecto_Grupo_trabajo_e8701ad4" ON "proyectos_proyecto_Grupo_trabajo" USING btree (user_id);
 ?   DROP INDEX public."proyectos_proyecto_Grupo_trabajo_e8701ad4";
       public         root    false    188    2280            �           1259    51774 )   proyectos_proyecto_Grupo_trabajo_f543c3f9    INDEX     z   CREATE INDEX "proyectos_proyecto_Grupo_trabajo_f543c3f9" ON "proyectos_proyecto_Grupo_trabajo" USING btree (proyecto_id);
 ?   DROP INDEX public."proyectos_proyecto_Grupo_trabajo_f543c3f9";
       public         root    false    188    2280            �           1259    51763 /   proyectos_proyecto_Nombre_5aa85695e8c06938_like    INDEX     �   CREATE INDEX "proyectos_proyecto_Nombre_5aa85695e8c06938_like" ON proyectos_proyecto USING btree ("Nombre" varchar_pattern_ops);
 E   DROP INDEX public."proyectos_proyecto_Nombre_5aa85695e8c06938_like";
       public         root    false    186    2280                       1259    52066 "   proyectos_proyecto_Tablas_bd1d5624    INDEX     i   CREATE INDEX "proyectos_proyecto_Tablas_bd1d5624" ON "proyectos_proyecto_Tablas" USING btree (flujo_id);
 8   DROP INDEX public."proyectos_proyecto_Tablas_bd1d5624";
       public         root    false    202    2280                       1259    52065 "   proyectos_proyecto_Tablas_f543c3f9    INDEX     l   CREATE INDEX "proyectos_proyecto_Tablas_f543c3f9" ON "proyectos_proyecto_Tablas" USING btree (proyecto_id);
 8   DROP INDEX public."proyectos_proyecto_Tablas_f543c3f9";
       public         root    false    202    2280            �           1259    51762    proyectos_proyecto_f4cd2b0a    INDEX     `   CREATE INDEX proyectos_proyecto_f4cd2b0a ON proyectos_proyecto USING btree ("Scrum_Master_id");
 /   DROP INDEX public.proyectos_proyecto_f4cd2b0a;
       public         root    false    186    2280            �           1259    52191    sprint_sprint_4580bcd4    INDEX     X   CREATE INDEX sprint_sprint_4580bcd4 ON sprint_sprint USING btree ("Tabla_asignada_id");
 *   DROP INDEX public.sprint_sprint_4580bcd4;
       public         root    false    184    2280            �           1259    51710    sprint_sprint_56ac0855    INDEX     Y   CREATE INDEX sprint_sprint_56ac0855 ON sprint_sprint USING btree ("Usuario_creador_id");
 *   DROP INDEX public.sprint_sprint_56ac0855;
       public         root    false    184    2280            �           1259    52172    sprint_sprint_80b83c89    INDEX     [   CREATE INDEX sprint_sprint_80b83c89 ON sprint_sprint USING btree ("Proyecto_asignado_id");
 *   DROP INDEX public.sprint_sprint_80b83c89;
       public         root    false    184    2280            �           1259    51711 *   sprint_sprint_Nombre_427388f816e1b2ae_like    INDEX     w   CREATE INDEX "sprint_sprint_Nombre_427388f816e1b2ae_like" ON sprint_sprint USING btree ("Nombre" varchar_pattern_ops);
 @   DROP INDEX public."sprint_sprint_Nombre_427388f816e1b2ae_like";
       public         root    false    184    2280            '           1259    52171 !   sprint_sprint_UserStorys_4d4c3b6a    INDEX     k   CREATE INDEX "sprint_sprint_UserStorys_4d4c3b6a" ON "sprint_sprint_UserStorys" USING btree (userstory_id);
 7   DROP INDEX public."sprint_sprint_UserStorys_4d4c3b6a";
       public         root    false    205    2280            (           1259    52170 !   sprint_sprint_UserStorys_b688f27b    INDEX     h   CREATE INDEX "sprint_sprint_UserStorys_b688f27b" ON "sprint_sprint_UserStorys" USING btree (sprint_id);
 7   DROP INDEX public."sprint_sprint_UserStorys_b688f27b";
       public         root    false    205    2280            -           1259    52353    userstory_cargarhoras_354ea2ca    INDEX     e   CREATE INDEX userstory_cargarhoras_354ea2ca ON userstory_cargarhoras USING btree ("US_asignado_id");
 2   DROP INDEX public.userstory_cargarhoras_354ea2ca;
       public         root    false    207    2280            �           1259    51689    userstory_userstory_5622a7cc    INDEX     f   CREATE INDEX userstory_userstory_5622a7cc ON userstory_userstory USING btree ("Usuario_asignado_id");
 0   DROP INDEX public.userstory_userstory_5622a7cc;
       public         root    false    182    2280            �           1259    51690    userstory_userstory_56ac0855    INDEX     e   CREATE INDEX userstory_userstory_56ac0855 ON userstory_userstory USING btree ("Usuario_creador_id");
 0   DROP INDEX public.userstory_userstory_56ac0855;
       public         root    false    182    2280            �           1259    51802    userstory_userstory_80b83c89    INDEX     g   CREATE INDEX userstory_userstory_80b83c89 ON userstory_userstory USING btree ("Proyecto_asignado_id");
 0   DROP INDEX public.userstory_userstory_80b83c89;
       public         root    false    182    2280            �           1259    52330    userstory_userstory_8f022ccb    INDEX     h   CREATE INDEX userstory_userstory_8f022ccb ON userstory_userstory USING btree ("Actividad_asignada_id");
 0   DROP INDEX public.userstory_userstory_8f022ccb;
       public         root    false    182    2280            �           1259    51691 0   userstory_userstory_Nombre_7484bc344fd54706_like    INDEX     �   CREATE INDEX "userstory_userstory_Nombre_7484bc344fd54706_like" ON userstory_userstory USING btree ("Nombre" varchar_pattern_ops);
 F   DROP INDEX public."userstory_userstory_Nombre_7484bc344fd54706_like";
       public         root    false    182    2280            <           2606    51803 >   Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id" FOREIGN KEY ("Proyecto_asignado_id") REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id";
       public       root    false    186    2038    182    2280            ?           2606    52173 >   Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id" FOREIGN KEY ("Proyecto_asignado_id") REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id";
       public       root    false    2038    184    186    2280            0           2606    51540 ?   auth_content_type_id_508cf46651277a81_fk_django_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id;
       public       root    false    166    1978    168    2280            1           2606    51658 6   auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT "auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id" FOREIGN KEY ("Usuario_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT "auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id";
       public       root    false    170    174    1997    2280            2           2606    51547 ?   auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id;
       public       root    false    170    1989    172    2280            3           2606    51552 ?   auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id;
       public       root    false    1983    168    172    2280            7           2606    51577 ?   auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id;
       public       root    false    168    1983    178    2280            5           2606    51565 ;   auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id;
       public       root    false    170    176    1989    2280            4           2606    51560 9   auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id;
       public       root    false    174    176    1997    2280            6           2606    51572 ?   auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id;
       public       root    false    178    1997    174    2280            8           2606    51596 ?   djan_content_type_id_697914295151027a_fk_django_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id;
       public       root    false    180    1978    166    2280            9           2606    51601 9   django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id;
       public       root    false    174    1997    180    2280            M           2606    52016 ?   flujos__userstory_id_526e93db1bd5d928_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_To_do"
    ADD CONSTRAINT flujos__userstory_id_526e93db1bd5d928_fk_userstory_userstory_id FOREIGN KEY (userstory_id) REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_To_do" DROP CONSTRAINT flujos__userstory_id_526e93db1bd5d928_fk_userstory_userstory_id;
       public       root    false    2023    182    200    2280            K           2606    52004 ?   flujos__userstory_id_6522e51beede21ba_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Done"
    ADD CONSTRAINT flujos__userstory_id_6522e51beede21ba_fk_userstory_userstory_id FOREIGN KEY (userstory_id) REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_Done" DROP CONSTRAINT flujos__userstory_id_6522e51beede21ba_fk_userstory_userstory_id;
       public       root    false    2023    182    198    2280            H           2606    52023 ?   flujos_a_userstory_id_4d15710c8b4bb70_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Doing"
    ADD CONSTRAINT flujos_a_userstory_id_4d15710c8b4bb70_fk_userstory_userstory_id FOREIGN KEY (userstory_id) REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_Doing" DROP CONSTRAINT flujos_a_userstory_id_4d15710c8b4bb70_fk_userstory_userstory_id;
       public       root    false    196    182    2023    2280            L           2606    52011 ?   flujos_act_actividad_id_187db8a228ca9d95_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_To_do"
    ADD CONSTRAINT flujos_act_actividad_id_187db8a228ca9d95_fk_flujos_actividad_id FOREIGN KEY (actividad_id) REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_To_do" DROP CONSTRAINT flujos_act_actividad_id_187db8a228ca9d95_fk_flujos_actividad_id;
       public       root    false    200    190    2047    2280            J           2606    51999 ?   flujos_act_actividad_id_21990a3cf36ff421_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Done"
    ADD CONSTRAINT flujos_act_actividad_id_21990a3cf36ff421_fk_flujos_actividad_id FOREIGN KEY (actividad_id) REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_Done" DROP CONSTRAINT flujos_act_actividad_id_21990a3cf36ff421_fk_flujos_actividad_id;
       public       root    false    198    190    2047    2280            I           2606    52028 ?   flujos_act_actividad_id_50a9a0ac31308f63_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_actividad_Doing"
    ADD CONSTRAINT flujos_act_actividad_id_50a9a0ac31308f63_fk_flujos_actividad_id FOREIGN KEY (actividad_id) REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_actividad_Doing" DROP CONSTRAINT flujos_act_actividad_id_50a9a0ac31308f63_fk_flujos_actividad_id;
       public       root    false    2047    190    196    2280            F           2606    51894 ?   flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id FOREIGN KEY (actividad_id) REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id;
       public       root    false    2047    190    194    2280            E           2606    51855 ?   flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY flujos_flujo
    ADD CONSTRAINT "flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.flujos_flujo DROP CONSTRAINT "flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id";
       public       root    false    174    1997    192    2280            G           2606    51899 ?   flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id" FOREIGN KEY (flujo_id) REFERENCES flujos_flujo(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id";
       public       root    false    2051    194    192    2280            A           2606    51782 ?   proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id";
       public       root    false    174    186    1997    2280            B           2606    51797 ?   proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id" FOREIGN KEY ("Scrum_Master_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id";
       public       root    false    174    1997    186    2280            C           2606    51787 ?   proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id";
       public       root    false    188    1997    174    2280            O           2606    52060 ?   proyectos_proyecto_flujo_id_564e6dc3cdd53746_fk_flujos_flujo_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Tablas"
    ADD CONSTRAINT proyectos_proyecto_flujo_id_564e6dc3cdd53746_fk_flujos_flujo_id FOREIGN KEY (flujo_id) REFERENCES flujos_flujo(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Tablas" DROP CONSTRAINT proyectos_proyecto_flujo_id_564e6dc3cdd53746_fk_flujos_flujo_id;
       public       root    false    202    192    2051    2280            D           2606    51792 ?   proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id;
       public       root    false    186    188    2038    2280            N           2606    52055 ?   proyectos_proyecto_id_42325383386b6038_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Tablas"
    ADD CONSTRAINT proyectos_proyecto_id_42325383386b6038_fk_proyectos_proyecto_id FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Tablas" DROP CONSTRAINT proyectos_proyecto_id_42325383386b6038_fk_proyectos_proyecto_id;
       public       root    false    186    202    2038    2280            P           2606    52242 ?   sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id FOREIGN KEY (userstory_id) REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id;
       public       root    false    182    205    2023    2280            @           2606    52197 ?   sprint_sp_Tabla_asignada_id_67d71e7b71206823_fk_flujos_flujo_id    FK CONSTRAINT     �   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "sprint_sp_Tabla_asignada_id_67d71e7b71206823_fk_flujos_flujo_id" FOREIGN KEY ("Tabla_asignada_id") REFERENCES flujos_flujo(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "sprint_sp_Tabla_asignada_id_67d71e7b71206823_fk_flujos_flujo_id";
       public       root    false    192    184    2051    2280            >           2606    51705 ?   sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id";
       public       root    false    1997    174    184    2280            Q           2606    52247 ?   sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id    FK CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id" FOREIGN KEY (sprint_id) REFERENCES sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id";
       public       root    false    205    184    2031    2280            =           2606    52331 ?   u_Actividad_asignada_id_1a44800c7a2e04c8_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "u_Actividad_asignada_id_1a44800c7a2e04c8_fk_flujos_actividad_id" FOREIGN KEY ("Actividad_asignada_id") REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "u_Actividad_asignada_id_1a44800c7a2e04c8_fk_flujos_actividad_id";
       public       root    false    2047    182    190    2280            R           2606    52348 ?   users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_cargarhoras
    ADD CONSTRAINT "users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id" FOREIGN KEY ("US_asignado_id") REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.userstory_cargarhoras DROP CONSTRAINT "users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id";
       public       root    false    182    2023    207    2280            :           2606    51679 ?   userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id" FOREIGN KEY ("Usuario_asignado_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id";
       public       root    false    174    1997    182    2280            ;           2606    51684 ?   userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id";
       public       root    false    1997    182    174    2280            �   6   x�3��M,.I-�4204�50�54W04�22�24�3�0061�50�4����� �J	_      �   �   x�����0��N0W@�v.�'�g�RI}�>59s:���>�ܧ7���{����.��BdTBAE4��*��J�F���rzq=_���<����9�������q=߸�\�/���ԋH��+��ːzY�^6�����C��e����1��L�97�m�z��z��zs���-�1      �   (  x�e�]�� ����`����^c������:I��W�(
�M�����4���b�s����L�s�<�~�K��_��*�B(��'��=C(�5JW�^z۴5�����f �	�RuƂ���gg��U^�yO�1�@�	�B<Pplʱ��=r!�����P����P��5��>���*�x	��5u�`pf|C�7Z��;�TxۭoV\t��Ā��zJĆti�}�q��W��|d7&Q� (���xY,Q*�]��IN��V\�Zʁ��5S�mP��ߖ^�y�Rẽ���"@�t���fg���'�W��D$`��Gv~H��J��P�*�ѣ��Pa!�p	�t�`�� ���|���ն��^=ѶC��X^g�Zl���Y��x��'7�d�n�S�`2� wп���o����?Kx�����x>������͹��ur+���O���j|_�ef5��y�C��F.��1�ɋ0��4^�ts쎉�_b>��l��t��тl���{F������b"�5�������e�G8�F�����k��      �     x�mO]O�@|>~Ex3Ż�8+��"���\)P�㐏��=����;�N6��Y�}~H�[{�*�B�,D��o�)���<�~��(|t�/�������]�?��~Γ�O#�":���d؈�k���)$��Pf��ɾ[a3�Q�[�@��fl���ܽ�6����C�Ћ_�\���e1s�-r�u��9ڦ=Zq�C[�5�@F�x6Y�yt�Q��H����oӒg��R������h�g�0qD�'��8^�-XgU�W0Y�NS�B�kK      �      x�3�4�4����� �Y      �      x������ � �      �   e   x�e�1�  ��~ �VQq�.D�:�����]r9!6�Z�]�� 40����`8\�|* 50�?�Zw�[2_/�g��ǧ����_�5����'��/ͻ�      �   �   x�]�[� E�gV�
��}�?�b�4q����u�=C���u���f��dl�b^�d��� c�w��E_|F�@dM�$�+(g�rYf�ג��o��l�%��w��f��ۀ7�H�Ǵ����e�	|�r�8{26�
��\qp�G$<���NR�;��;St�(��e9�c�너_2�8      �   �  x��Y[�9���b/A��9�g�;�bb�� ��j�n�����`�Z"�dQK����ٝN>7Ǖ����n{ڮ?Vl)|����(~��ݲ)9��߬���|��ူ6�p��ۯ���&\���#<��~�s�8���*�eGp��n8l~�o��qs�?�����v��bb.#C��s��]�a��	��{���*8Q)T��'p`��*8�B�	���~?�ϟ��y}��Ux�>�zp�>?C��
�	X��p0�RJT��>t�|��	H��[b�O*#~CdN8)����\�O�"��x�-R���W��({R�� X�jYФ.�34[֤M���Z�4ɋ�@�a�;�CTo̓�(t������
��fZ�Ux<�u�d�#rǫ��a�;=�.�aׁX�!P���mU{yX����0dc9Y_�A2�.��}�&r�y��ټ��;|6!�T���ĉ �#���RD/	˒�-��g�1\�^$�_08-���T鬤
�ɶ�9�9�HR�����h�(�Qʹ�,�)��,^���q��[�i�_L@�V|Lp��k{֯���͒�,�Eh��c&O9h
~�RPI��JV�|��}(*�R��-�	E��S�E�%����fe��*�$B*9pSC��~>�3jN�3AM����/F{q�)����qO�6����D�֥�����zg�N��.���Wqw�8�����s�V�%�҆�w0-?��9(��+�w�'G�KLU���\�ᙵ�|N1�~�������4�ɉ|��Zb���W�W.����|��O2E��=?��FqZ��X+c���o�<�Ƹ[5�#�,�l�h��޶��g�#D`�b;K��)�Ȫղ��j?�qN0�5EZYF���%��y�CMZ�`	�Vv�"�)�M����䤞������d�bLV��
]�4f�Ee�%�IR��Ǝ4]`j#J��BJ��J�Ȱͤu9�m���'��ڪ�aF��9�R�����v�bRȗ>�6�E)��q��QHq�[R(� E��%[,�8�/(X��<�ML�*�(��aI�L^�䃝�5�Q���"hu
���Aj��6��1�*�S�-�R��g��%�kO-!eu��X��\D'�IH����yߌ��l��zm։:��p~`)��^?��L����w�$�r��=I�M����6@�GSi��:]��9|qzo�XlUA)t��&�tX�0O;�b��fX������S��Ŵk��)�1�}(�6Ɣ;<�iYƗMya|2+mM�Ë1��E^khq���˝gC��<�1V�DU��S ���u\�x�O��U��e�]�5��� ��})���s'A1��AOI�1���s'BJ�;�=C1�mlG�D����ƕ�ۛ@�����n�;)��؀��b;�iv�� �QVڻ\��'G�]c��`��fOr�[�s��q�P� E�.J	YE (08-�E�.����:���q3ljGھ��:?�/���)�jQS�@Ꝃ�%p��E�Ҳ�Ɲ������}u��4j�u}x_~��w�X�M���"�x�i��5�钱���()DYaņ_P�2P�/]m)-IR�.+������.�'��%E~���"��.ٔ
E��O$��� ��=����E��H~|��;o�9�-�
]���J�W��N��/R��Ћ׻/�`�ƕ�=�Z�QX�'9��룾�({Aq�y4�t	��*/�	yt� ᘙȲ�o7��)�8�6�6///�6<�      �   �  x���Ao�0��ɯ�?��p�UI`A����B�6��__��^v�=�q�Fo����:}�^��p@�R�ԛ���>�vAy�h�u�T�%k١n$� @LTU#�e�TAf�!Tl��:�.��[f%Ff�5�=��M�d��D��d-�e���b���C;
*�R�G�xa��B=5�}xY�r��$Sa-��^t�DM���$8� w(��!���ｳ9��S��=֞�!�>���3����. a�B��?�f���5���W�^���d�����4����BSw�=.g�@�r�񮥼V���#�1��n�hKM-
G$y�1�/n1a��c:���1K�h���l� :T�<+�{���
S.�3��On�v���`B��=����#�̪      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     